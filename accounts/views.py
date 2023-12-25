from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, CustomUserDetailsSerializer
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404
from allauth.account.models import EmailConfirmation
from allauth.account.utils import complete_signup
from .models import CustomUser
from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['POST'])
@permission_classes([AllowAny])
def enter_verification_code(request):
    if request.method == 'POST':
        verification_code = request.data.get('verification_code')
        phone_number = request.data.get('phone_number')

        try:
            user = CustomUser.objects.get(
                phone_number=phone_number, verification_code=verification_code)
        except CustomUser.DoesNotExist:
            return Response({'detail': 'Invalid verification code or phone number.'}, status=status.HTTP_400_BAD_REQUEST)

        user.user_verified = True
        user.save()

        return Response({'detail': 'Phone number verified successfully.'}, status=status.HTTP_200_OK)


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=request.data['username'])

        verification_code = get_random_string(
            length=4, allowed_chars='1234567890')
        user.verification_code = verification_code
        user.save()

        subject = 'Welcome to Project 8'
        message = 'This project is realized by awesome SAM team! Sardana, Assyl, Margulan'
        from_email = 'assyl.akhambay@gmail.com'
        recipient_list = user.email

        send_mail(subject, message, from_email, [recipient_list])

        return response


class CustomUserDetailsView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        existing_profile_image = serializer.instance.profile_image
        existing_phone_number = serializer.instance.phone_number
        serializer.save()

        if 'profile_image' not in self.request.data or not self.request.data['profile_image']:
            serializer.instance.profile_image = existing_profile_image
            serializer.instance.save()

        new_phone_number = self.request.data.get('phone_number', None)
        if new_phone_number != existing_phone_number:
            serializer.instance.user_verified = False
            serializer.instance.save()
            verification_code = get_random_string(
                length=4, allowed_chars='1234567890')
            serializer.instance.verification_code = verification_code
            serializer.instance.save()

            subject = 'Verify Your Phone Number. Project 8'
            message = f'Your verification code is: {verification_code}'
            from_email = 'assyl.akhambay@gmail.com'
            recipient_list = [serializer.instance.email]

            send_mail(subject, message, from_email, recipient_list)

        return Response({'detail': 'Profile updated successfully.'}, status=status.HTTP_200_OK)
