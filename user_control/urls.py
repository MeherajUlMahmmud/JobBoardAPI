from django.urls import path

from user_control.views.applicant import (
    GetApplicantListAPIView, GetApplicantDetailsAPIView, UpdateApplicantDetailsAPIView,
)
from user_control.views.organization import (
    GetOrganizationListAPIView, GetOrganizationDetailsAPIView, UpdateOrganizationDetailsAPIView,
)
from user_control.views.user import (
    GetUserListAPIView, CreateUserAPIView, GetUserDetailsAPIView, UpdateUserDetailsAPIView, GetUserProfileAPIView,
)

urlpatterns = [
    # User URLs
    path('user/', GetUserListAPIView.as_view(), name='get_user_list'),
    path('user/create/', CreateUserAPIView.as_view(), name='create_user'),
    path('user/profile/', GetUserProfileAPIView.as_view(), name='get_user_profile'),
    path('user/<str:pk>/details/', GetUserDetailsAPIView.as_view(), name='get_user_details'),
    path('user/<str:pk>/update/', UpdateUserDetailsAPIView.as_view(), name='update_user_details'),

    # Applicant URLs
    path('applicant/', GetApplicantListAPIView.as_view(), name='get_applicant_list'),
    path('applicant/<str:pk>/details/', GetApplicantDetailsAPIView.as_view(), name='get_applicant_details'),
    path('applicant/<str:pk>/update/', UpdateApplicantDetailsAPIView.as_view(), name='update_applicant_details'),

    # Organization URLs
    path('organization/', GetOrganizationListAPIView.as_view(), name='get_organization_list'),
    path('organization/<str:pk>/details/', GetOrganizationDetailsAPIView.as_view(), name='get_organization_details'),
    path('organization/<str:pk>/update/', UpdateOrganizationDetailsAPIView.as_view(),
         name='update_organization_details'),

]
