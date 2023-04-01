from rest_framework import routers
from django.urls import path, include

from resume_control.views.award import AwardModelViewSet
from resume_control.views.certification import CertificationModelViewSet
from resume_control.views.education import EducationModelViewSet
from resume_control.views.experience import ExperienceModelViewSet
from resume_control.views.interest import InterestModelViewSet
from resume_control.views.language import LanguageModelViewSet
from resume_control.views.personal import PersonalModelViewSet
from resume_control.views.reference import ReferenceModelViewSet
from resume_control.views.resume import ResumeModelViewSet
from resume_control.views.skill import SkillModelViewSet

router = routers.DefaultRouter()
router.register(r'api/resume', ResumeModelViewSet, basename='resume')
router.register(r'api/personal', PersonalModelViewSet, basename='personal')
# router.register(r'api/contact', ContactModelViewSet, basename='contact')
router.register(r'api/experience', ExperienceModelViewSet, basename='experience')
router.register(r'api/education', EducationModelViewSet, basename='education')
router.register(r'api/skill', SkillModelViewSet, basename='skill')
router.register(r'api/language', LanguageModelViewSet, basename='language')
router.register(r'api/interest', InterestModelViewSet, basename='interest')
router.register(r'api/reference', ReferenceModelViewSet, basename='reference')
router.register(r'api/award', AwardModelViewSet, basename='award')
router.register(r'api/certification', CertificationModelViewSet, basename='certification')

urlpatterns = [
    path('', include(router.urls)),
]
