from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('list', views.UserAPIView.as_view()),
    path('get/<str:pk>', views.UserAPIView.as_view()),
    # path('user/update/<str:pk>', views.UserAPIView.as_view()),
]
