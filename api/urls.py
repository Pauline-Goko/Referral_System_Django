from django.urls import path
from .views import GenerateReferralLink, TrackSignup, GetReferralStatusAndReward

urlpatterns = [
    path('referral/generate/', GenerateReferralLink.as_view()),
    path('referral/signup/', TrackSignup.as_view()),
    path('referral/status/', GetReferralStatusAndReward.as_view()),
]
