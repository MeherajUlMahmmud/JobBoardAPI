from django.urls import path

from resume_control.views.award import (
    GetAwardListAPIView, GetAwardDetailsAPIView, CreateAwardAPIView, UpdateAwardDetailsAPIView,
)
from resume_control.views.certification import (
    CreateCertificationAPIView, GetCertificationDetailsAPIView, GetCertificationListAPIView,
    UpdateCertificationDetailsAPIView,
)
from resume_control.views.contact import (
    GetContactDetailsAPIView, UpdateContactDetailsAPIView,
)
from resume_control.views.education import (
    GetEducationListAPIView, GetEducationDetailsAPIView, CreateEducationAPIView, UpdateEducationDetailsAPIView,
)
from resume_control.views.experience import (
    GetExperienceListAPIView, GetExperienceDetailsAPIView, CreateExperienceAPIView, UpdateExperienceDetailsAPIView,
)
from resume_control.views.interest import (
    CreateInterestAPIView, GetInterestListAPIView, GetInterestDetailsAPIView, UpdateInterestDetailsAPIView,
)
from resume_control.views.language import (
    CreateLanguageAPIView, GetLanguageListAPIView, GetLanguageDetailsAPIView, UpdateLanguageDetailsAPIView,
)
from resume_control.views.personal import (
    GetPersonalDetailsAPIView, UpdatePersonalDetailsAPIView,
)
from resume_control.views.reference import (
    CreateReferenceAPIView, GetReferenceListAPIView, GetReferenceDetailsAPIView, UpdateReferenceDetailsAPIView,
)
from resume_control.views.resume import (
    GetResumeListAPIView, CreateResumeAPIView, GetResumeDetailsAPIView,
)
from resume_control.views.skill import (
    CreateSkillAPIView, GetSkillListAPIView, GetSkillDetailsAPIView, UpdateSkillDetailsAPIView,
)

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

    # Experience URLs
    path('experience/<str:resume_id>/', GetExperienceListAPIView.as_view(), name='get_experience_list'),
    path('experience/<str:pk>/details/', GetExperienceDetailsAPIView.as_view(), name='get_experience_details'),
    path('experience/create/', CreateExperienceAPIView.as_view(), name='create_experience_list'),
    path('experience/<str:pk>/update/', UpdateExperienceDetailsAPIView.as_view(), name='update_experience_details'),

    # Education URLs
    path('education/<str:resume_id>/', GetEducationListAPIView.as_view(), name='get_education_list'),
    path('education/<str:pk>/details/', GetEducationDetailsAPIView.as_view(), name='get_education_details'),
    path('education/create/', CreateEducationAPIView.as_view(), name='create_education_list'),
    path('education/<str:pk>/update/', UpdateEducationDetailsAPIView.as_view(), name='update_education_details'),

    # Skill URLs
    path('skill/create/', CreateSkillAPIView.as_view(), name='create_skill_list'),
    path('skill/<str:resume_id>/', GetSkillListAPIView.as_view(), name='get_skill_list'),
    path('skill/<str:pk>/details/', GetSkillDetailsAPIView.as_view(), name='get_skill_details'),
    path('skill/<str:pk>/update/', UpdateSkillDetailsAPIView.as_view(), name='update_skill_details'),

    # Language URLs
    path('language/create/', CreateLanguageAPIView.as_view(), name='create_language_list'),
    path('language/<str:resume_id>/', GetLanguageListAPIView.as_view(), name='get_language_list'),
    path('language/<str:pk>/details/', GetLanguageDetailsAPIView.as_view(), name='get_language_details'),
    path('language/<str:pk>/update/', UpdateLanguageDetailsAPIView.as_view(), name='update_language_details'),

    # Interest URLs
    path('interest/create/', CreateInterestAPIView.as_view(), name='create_interest_list'),
    path('interest/<str:resume_id>/', GetInterestListAPIView.as_view(), name='get_interest_list'),
    path('interest/<str:pk>/details/', GetInterestDetailsAPIView.as_view(), name='get_interest_details'),
    path('interest/<str:pk>/update/', UpdateInterestDetailsAPIView.as_view(), name='update_interest_details'),

    # Reference URLs
    path('reference/create/', CreateReferenceAPIView.as_view(), name='create_reference_list'),
    path('reference/<str:resume_id>/', GetReferenceListAPIView.as_view(), name='get_reference_list'),
    path('reference/<str:pk>/details/', GetReferenceDetailsAPIView.as_view(), name='get_reference_details'),
    path('reference/<str:pk>/update/', UpdateReferenceDetailsAPIView.as_view(), name='update_reference_details'),

    # Certification URLs
    path('certification/create/', CreateCertificationAPIView.as_view(), name='create_certification_list'),
    path('certification/<str:resume_id>/', GetCertificationListAPIView.as_view(), name='get_certification_list'),
    path('certification/<str:pk>/details/', GetCertificationDetailsAPIView.as_view(), name='get_certification_details'),
    path(
        'certification/<str:pk>/update/',
        UpdateCertificationDetailsAPIView.as_view(),
        name='update_certification_details',
    ),

    # Award URLs
    path('award/create/', CreateAwardAPIView.as_view(), name='create_award_list'),
    path('award/<str:resume_id>/', GetAwardListAPIView.as_view(), name='get_award_list'),
    path('award/<str:pk>/details/', GetAwardDetailsAPIView.as_view(), name='get_award_details'),
    path('award/<str:pk>/update/', UpdateAwardDetailsAPIView.as_view(), name='update_award_details'),
]
