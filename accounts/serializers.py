from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class CustomRegisterSerializer(RegisterSerializer):
    def custom_signup(self, request, user):
        user.save()


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('pk', 'username', 'email', 'first_name',
                  'last_name', 'DOB', 'phone_number', 'profile_image', 'token')
        read_only_fields = ['email']

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


"""
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
        
        existing_profile_image = serializer.instance.profile_image
        serializer.save()

        if 'profile_image' not in self.request.data or not self.request.data['profile_image']:
            serializer.instance.profile_image = existing_profile_image
            serializer.instance.save()
"""
