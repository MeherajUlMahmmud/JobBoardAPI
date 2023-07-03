from django.urls import path, include
from rest_framework import routers

from job_control.views.job import JobModelViewSet
from job_control.views.job_type import JobTypeModelViewSet

router = routers.DefaultRouter()
router.register(r'api/job-type', JobTypeModelViewSet, basename='job-type')
router.register(r'api/job', JobModelViewSet, basename='job')
# router.register(r'api/job-application', JobApplicationModelViewSet, basename='job-application')

urlpatterns = [
    path('', include(router.urls)),
]
