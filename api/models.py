from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.crypto import get_random_string

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    referrer_email = models.EmailField(null=True, blank=True)
    referrer_name = models.CharField(max_length=255, null=True, blank=True)

    user_permissions = models.ManyToManyField('auth.Permission', related_name='api_users', blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='api_users', blank=True)
    
class Referral(models.Model):
    referrer_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrer_referrals')
    unique_code = models.CharField(max_length=10, unique=True)
    referred_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    reward = models.CharField(max_length=255, blank=True)

    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE, related_name='user_referrals')

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = get_random_string()
        super().save(*args, **kwargs) 

    def calculate_reward(self):
        if self.status == 'success':
            return 1
        else:
            return 0                          