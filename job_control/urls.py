from django.urls import path

from job_control.views.job_type import (
    CreateJobTypeAPIView, GetJobTypeListAPIView, GetJobTypeDetailsAPIView, UpdateJobTypeDetailsAPIView,
)

# router.register(r'api/job', JobModelViewSet, basename='job')
# router.register(r'api/job-application', JobApplicationModelViewSet, basename='job-application')

urlpatterns = [
    # Job Type URLs
    path('job-type/', GetJobTypeListAPIView.as_view(), name='get_job_type_list'),
    path('job-type/create/', CreateJobTypeAPIView.as_view(), name='create_job_type'),
    path('job-type/<str:pk>/details/', GetJobTypeDetailsAPIView.as_view(), name='get_job_type_details'),
    path('job-type/<str:pk>/update/', UpdateJobTypeDetailsAPIView.as_view(), name='update_job_type_details'),

]
