from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, CustomUserDetailsSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404
from allauth.account.models import EmailConfirmation
from allauth.account.utils import complete_signup
from .models import CustomUser
from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

"""
class EnterVerificationCodeView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailsSerializer

    def create(self, request, *args, **kwargs):
        verification_code = request.data.get('verification_code')
        user = get_object_or_404(
            CustomUser, pk=self.request.user.pk, verification_code=verification_code)

        user.user_verified = True
        user.save()

        return Response({'detail': 'Profile verified successfully.'}, status=status.HTTP_200_OK)
"""


@api_view(['POST'])
@permission_classes([AllowAny])
def enter_verification_code(request):
    if request.method == 'POST':
        verification_code = request.data.get('verification_code')
        email = request.data.get('email')

        try:
            user = CustomUser.objects.get(
                email=email, verification_code=verification_code)
        except CustomUser.DoesNotExist:
            return Response({'detail': 'Invalid verification code or email.'}, status=status.HTTP_400_BAD_REQUEST)

        user.user_verified = True
        user.save()

        return Response({'detail': 'Email verified successfully.'}, status=status.HTTP_200_OK)


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=request.data['username'])

        verification_code = get_random_string(
            length=4, allowed_chars='1234567890')
        user.verification_code = verification_code
        user.save()

        subject = 'Verify Your Email'
        message = f'Your verification code is: {verification_code}'
        from_email = 'assyl.akhambay@gmail.com'
        to_email = user.email

        send_mail(subject, message, from_email, [to_email])

        return response


class CustomUserDetailsView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailsSerializer

    def get_object(self):
        return self.request.user
