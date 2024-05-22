# In admin.py

from django import forms
from django.contrib import admin
from django.utils.crypto import get_random_string

from .models import Referral

class ReferralAdminForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = '__all__'
        widgets = {
            'unique_code': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make the unique code field read-only
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
          
            self.fields['unique_code'].initial = get_random_string(10)

        def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
        if not self.instance.pk:
            
            self.instance.reward = self.instance.calculate_reward()

class ReferralAdmin(admin.ModelAdmin):
    form = ReferralAdminForm

admin.site.register(Referral, ReferralAdmin)
