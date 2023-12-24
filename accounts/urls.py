from django.urls import path
from .views import CustomRegisterView, CustomUserDetailsView, enter_verification_code
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('registration/', CustomRegisterView.as_view(),
         name='custom-registration'),
    path('profile/', CustomUserDetailsView.as_view(),
         name='custom-user-details'),
    path('enter-verification-code/', enter_verification_code,
         name='enter-verification-code'),
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
