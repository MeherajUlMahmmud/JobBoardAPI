from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('verify-email', VerifyEmailAPIView.as_view(), name="verify-email"),
    path('resend-verification-email', ResendVerificationEmailAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutAPIView.as_view(), name="logout"),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('request-reset-email', RequestPasswordResetEmail.as_view(),
    #      name="request-reset-email"),
    # path('password-reset/<uidb64>/<token>',
    #      PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    # path('password-reset-complete', SetNewPasswordAPIView.as_view(),
    #      name='password-reset-complete')
]
