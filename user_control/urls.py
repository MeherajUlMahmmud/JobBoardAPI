from rest_framework import routers
from django.urls import path, include

from user_control.views.applicant import ApplicantModelViewSet
from user_control.views.organization import OrganizationModelViewSet
from user_control.views.user import UserModelViewSet

router = routers.DefaultRouter()
router.register(r'api/user', UserModelViewSet, basename='user')
router.register(r'api/applicant', ApplicantModelViewSet, basename='applicant')
router.register(r'api/organization', OrganizationModelViewSet, basename='organization')

urlpatterns = [
    path('', include(router.urls)),
]
