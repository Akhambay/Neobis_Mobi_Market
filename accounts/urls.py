from django.urls import path
from .views import CustomRegisterView, CustomUserDetailsView, enter_verification_code

urlpatterns = [
    path('registration/', CustomRegisterView.as_view(),
         name='custom-registration'),
    path('profile/', CustomUserDetailsView.as_view(),
         name='custom-user-details'),
    path('enter-verification-code/', enter_verification_code,
         name='enter-verification-code'),
]
