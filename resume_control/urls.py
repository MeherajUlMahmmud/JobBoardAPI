from django.urls import path

from resume_control.views import *

urlpatterns = [
    path('experience', ExperienceAPIView.as_view()),
    path('education', EducationAPIView.as_view()),
    path('skill', SkillAPIView.as_view()),
    path('language', LanguageAPIView.as_view()),
    path('interest', InterestAPIView.as_view()),
    path('reference', ReferenceAPIView.as_view()),
    path('award', AwardAPIView.as_view()),
    path('certification', CertificationAPIView.as_view()),
]
