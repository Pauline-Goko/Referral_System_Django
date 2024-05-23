from django.db import models
from django.contrib.auth.models import User
import uuid

class Referral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE)
    unique_code = models.CharField(max_length=40, unique=True)
    referred_email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('SUCCESS', 'Success')], default='PENDING')
    reward = models.IntegerField(blank=True, null=True)  

    def calculate_reward(referrer):
     if referrer.status == 'SUCCESS':
        return 1
     return 0
 
 

