from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser


class CustomRegisterSerializer(RegisterSerializer):
    def custom_signup(self, request, user):
        user.save()


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'username', 'email', 'first_name',
                  'last_name', 'DOB', 'phone_number', 'profile_image')
