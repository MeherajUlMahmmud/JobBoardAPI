from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    # path('verify-email/', VerifyEmailAPIView.as_view(), name="verify-email"),
    # path('resend-verification-email/', ResendVerificationEmailAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('password-change/', PasswordChangeAPIView.as_view(), name="password_change"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-password-reset/', RequestPasswordResetAPIView.as_view(), name="request_password_reset"),
    path('password-reset/<uidb64>/<token>/', PasswordResetAPIView.as_view(), name='password_reset_confirm'),
]
