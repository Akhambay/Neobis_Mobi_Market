from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class CustomRegisterSerializer(RegisterSerializer):
    def custom_signup(self, request, user):
        user.save()


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'username', 'email', 'first_name',
                  'last_name', 'DOB', 'phone_number', 'profile_image', 'password', 'token')

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
