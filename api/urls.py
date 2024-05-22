from django.urls import path
from .views import ReferralLinkGenerateView, SignupTrackingView, ReferralStatusCheckView

urlpatterns = [
    path('referral/generate/', ReferralLinkGenerateView.as_view(), name='referral-generate'),
    path('referral/signup/', SignupTrackingView.as_view(), name='referral-signup'),
    path('referral/status/', ReferralStatusCheckView.as_view(), name='referral-status'),
]
