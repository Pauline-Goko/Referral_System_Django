from rest_framework import generics, status
from rest_framework.response import Response
from .models import User, Referral
from .serializers import UserSerializer, ReferralSerializer
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

User = get_user_model()

class ReferralLinkGenerateView(generics.CreateAPIView):
    serializer_class = ReferralSerializer

    def post(self, request, *args, **kwargs):
        referrer_id = request.data.get('referrer_id')
        referred_email = request.data.get('referred_email')
        if not referrer_id or not referred_email:
            return Response({'error': 'Referrer ID and Referred Email are required.'}, status=status.HTTP_400_BAD_REQUEST)

        referrer = User.objects.get(id=referrer_id)
        unique_code = get_random_string(10)
        referral = Referral.objects.create(referrer=referrer, unique_code=unique_code, referred_email=referred_email)
        return Response({'referral_link': f"/api/referral/signup/?code={unique_code}"}, status=status.HTTP_201_CREATED)

class SignupTrackingView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        unique_code = request.data.get('code')
        # print (f"here is my code => {request.data}")
        if not unique_code:
            return Response({'error': 'Referral code is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        referral = Referral.objects.filter(unique_code=unique_code, status='Pending').first()
        if not referral:
            return Response({'error': 'Invalid or expired referral code.'}, status=status.HTTP_400_BAD_REQUEST)
        
        email = request.data.get('email')
        name = request.data.get('name')
        password = request.data.get('password')
        
        if not email or not name or not password:
            return Response({'error': 'Email, name, and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        new_user_data = {
            'email': email,
            'name': name,
            'password': password,
            'referrer_email': referral.referrer.email,
            'referrer_name': referral.referrer.name
        }
        
        user_serializer = UserSerializer(data=new_user_data)
        if user_serializer.is_valid():
            new_user = user_serializer.save()
            referral.status = 'True'
            referral.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReferralStatusCheckView(generics.ListAPIView):
    serializer_class = ReferralSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if not user_id:
            return Referral.objects.none()
        return Referral.objects.filter(referrer_id=user_id)
