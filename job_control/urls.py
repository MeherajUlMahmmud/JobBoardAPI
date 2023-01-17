from django.urls import path

from .views import *

urlpatterns = [
    path('job-type', JobTypeAPIView.as_view()),
    path('job', JobAPIView.as_view()),
    path('job-application', JobApplicationAPIView.as_view()),
]
