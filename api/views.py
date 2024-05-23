from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Referral
from .serializers import ReferralSerializer
import uuid

class GenerateReferralLink(APIView):
    def get(self, request):
        user = request.user  
        unique_code = str(uuid.uuid4())[:8].upper()
        while Referral.objects.filter(unique_code=unique_code).exists():
            unique_code = str(uuid.uuid4())[:8].upper()

        referral = Referral.objects.create(referrer=user, unique_code=unique_code)
        serializer = ReferralSerializer(referral)
        return Response(serializer.data)

class TrackSignup(APIView):
    def post(self, request):
        referred_email = request.data.get('referred_email')
        referral_code = request.data.get('referral_code')

        if not referred_email or not referral_code:
            return Response({'error': 'Missing required fields'}, status=400)

    
        try:
            referral = Referral.objects.get(unique_code=referral_code)
        except Referral.DoesNotExist:
            return Response({'error': 'Invalid referral code'}, status=400)

    
        if referred_email == referral.referrer.email or User.objects.filter(email=referred_email).exists():
            return Response({'error': 'Invalid referral email'}, status=400)

        referral.referred_email = referred_email
        referral.status = 'SUCCESS'
        referral.save()

        serializer = ReferralSerializer(referral)
        return Response(serializer.data)

class GetReferralStatusAndReward(APIView):
    def get(self, request):
        user = request.user  

        try:
            referral = Referral.objects.get(referrer=user)
        except Referral.DoesNotExist:
            referral = Referral.objects.create(referrer=user)

        
        referral.reward = calculate_reward(referral)
        referral.save()

        serializer = ReferralSerializer(referral)
        return Response(serializer.data)

def calculate_reward(referral):
    if referral.status == 'SUCCESS':
        return 1
    return 0