from rest_framework import serializers
from .models import CustomUser


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "first_name",
            "last_name",
            "DOB",
            "phone_number",
            "profile_image",
        )
        model = CustomUser
