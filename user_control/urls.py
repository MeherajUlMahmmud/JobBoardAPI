from django.urls import path, include
from rest_framework import routers

from user_control.views.applicant import ApplicantModelViewSet
from user_control.views.organization import OrganizationModelViewSet
from user_control.views.user import (
    GetUserListAPIView, CreateUserAPIView, GetUserDetailsAPIView, UpdateUserDetailsAPIView, GetUserProfileAPIView,
)

router = routers.DefaultRouter()
router.register(r'applicant', ApplicantModelViewSet, basename='applicant')
router.register(r'organization', OrganizationModelViewSet, basename='organization')

urlpatterns = [
    path('', include(router.urls)),

    # User URLs
    path('user/', GetUserListAPIView.as_view(), name='get_user_list'),
    path('user/create/', CreateUserAPIView.as_view(), name='create_user'),
    path('user/profile/', GetUserProfileAPIView.as_view(), name='get_user_profile'),
    path('user/<str:pk>/details/', GetUserDetailsAPIView.as_view(), name='get_user_details'),
    path('user/<str:pk>/update/', UpdateUserDetailsAPIView.as_view(), name='update_user_details'),
]
