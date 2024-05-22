from rest_framework import serializers
from .models import User, Referral

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'referrer_name', 'referrer_email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            referrer_email=validated_data.get('referrer_email'),
            referrer_name=validated_data.get('referrer_name'),
            password=validated_data['password']
        )
        return user


class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ['id', 'referrer_name', 'unique_code', 'referred_email', 'created_at', 'status']
