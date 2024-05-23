from django.contrib import admin
from .models import Referral
import uuid


class ReferralAdmin(admin.ModelAdmin):
    list_display = ('referrer', 'unique_code', 'referred_email')
    readonly_fields = ['unique_code', "referred_email"]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.unique_code = uuid.uuid4().hex[:8].upper()
            obj.reward = obj.calculate_reward()
            obj.referred_email = request.user.email  

        super().save_model(request, obj, form, change)



admin.site.register(Referral, ReferralAdmin)
