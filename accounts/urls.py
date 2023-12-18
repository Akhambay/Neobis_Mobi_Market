from django.urls import path
from .views import ProfileDetail, CustomRegisterView, CustomUserDetailsView, enter_verification_code

urlpatterns = [
    path('registration/', CustomRegisterView.as_view(),
         name='custom-registration'),
    path("<int:pk>/", ProfileDetail.as_view(), name="profile_page"),
    path('user-details/', CustomUserDetailsView.as_view(),
         name='custom-user-details'),
    path('enter-verification-code/', enter_verification_code,
         name='enter-verification-code'),
]
