from django.urls import path

from resume_control.views.contact import (
    GetContactDetailsAPIView, UpdateContactDetailsAPIView,
)
from resume_control.views.personal import (
    GetPersonalDetailsAPIView, UpdatePersonalDetailsAPIView,
)
from resume_control.views.resume import (
    GetResumeListAPIView, CreateResumeAPIView, GetResumeDetailsAPIView,
)

# router = routers.DefaultRouter()
# router.register(r'api/personal', PersonalModelViewSet, basename='personal')
# router.register(r'api/contact', ContactModelViewSet, basename='contact')
# router.register(r'api/experience', ExperienceModelViewSet, basename='experience')
# router.register(r'api/education', EducationModelViewSet, basename='education')
# router.register(r'api/skill', SkillModelViewSet, basename='skill')
# router.register(r'api/language', LanguageModelViewSet, basename='language')
# router.register(r'api/interest', InterestModelViewSet, basename='interest')
# router.register(r'api/reference', ReferenceModelViewSet, basename='reference')
# router.register(r'api/award', AwardModelViewSet, basename='award')
# router.register(r'api/certification', CertificationModelViewSet, basename='certification')

urlpatterns = [
    # Resume URLs
    path('resume/', GetResumeListAPIView.as_view()),
    path('resume/create/', CreateResumeAPIView.as_view(), name='create_resume'),
    path('resume/<str:pk>/details/', GetResumeDetailsAPIView.as_view(), name='get_resume_details'),

    # Personal URLs
    path('personal/<str:pk>/details/', GetPersonalDetailsAPIView.as_view(), name='get_personal_details'),
    path('personal/<str:pk>/update/', UpdatePersonalDetailsAPIView.as_view(), name='update_personal_details'),

    # Contact URLs
    path('contact/<str:pk>/details/', GetContactDetailsAPIView.as_view(), name='get_contact_details'),
    path('contact/<str:pk>/update/', UpdateContactDetailsAPIView.as_view(), name='update_contact_details'),
]
