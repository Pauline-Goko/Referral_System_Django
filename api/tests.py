from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import User, Referral
from .views import ReferralLinkGenerateView, SignupTrackingView, ReferralStatusCheckView
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='password', name='Test User')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.name, 'Test User')

class ReferralModelTest(TestCase):
    def test_referral_creation(self):
        user = User.objects.create_user(username='referrer', email='referrer@example.com', password='password', name='Referrer')
        referral = Referral.objects.create(referrer_name=user, unique_code='abcd', referred_email='referred@example.com', user=user)
        self.assertEqual(referral.referrer_name, user)
        self.assertEqual(referral.unique_code, 'abcd')
        self.assertEqual(referral.referred_email, 'referred@example.com')
        self.assertEqual(referral.user, user)

class ReferralLinkGenerateViewTest(TestCase):
    def test_referral_link_generation(self):
        url = reverse('referral-generate')
        response = self.client.post(url, {'referrer_id': 1, 'referred_email': 'test@example.com'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) 

class SignupTrackingViewTest(TestCase):
    def test_invalid_referral_code(self):
        url = reverse('referral-signup')
        response = self.client.post(url, {'code': 'invalid_code', 'email': 'test@example.com', 'name': 'Test User', 'password': 'password'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  

class ReferralStatusCheckViewTest(TestCase):
    def test_missing_user_id(self):
        url = reverse('referral-status')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
