from django.urls import path

from .views import *

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('refresh-token', ObtainAuthToken.as_view()),
    path('logout', LogoutAPIView.as_view()),
]
