from django.forms import Select, TextInput
from django_filters.rest_framework import (
    FilterSet, BooleanFilter, CharFilter, DateFromToRangeFilter,
)

from common.custom_widgets import CustomDateRangeFilterWidget
from user_control.models import UserModel, ApplicantModel, OrganizationModel


class UserModelFilter(FilterSet):
    is_verified = BooleanFilter(
        field_name="is_verified", label="Is Verified",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[(None, '---------'), (True, 'Yes'), (False, 'No')],
        )
    )
    is_applicant = BooleanFilter(
        field_name="is_applicant", label="Is Applicant",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[(None, '---------'), (True, 'Yes'), (False, 'No')],
        )
    )
    is_organization = BooleanFilter(
        field_name="is_organization", label="Is Organization",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[(None, '---------'), (True, 'Yes'), (False, 'No')],
        )
    )
    is_staff = BooleanFilter(
        field_name="is_staff", label="Is Staff",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[(None, '---------'), (True, 'Yes'), (False, 'No')],
        )
    )
    is_admin = BooleanFilter(
        field_name="is_admin", label="Is Admin",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[(None, '---------'), (True, 'Yes'), (False, 'No')],
        )
    )
    is_superuser = BooleanFilter(
        field_name="is_superuser", label="Is Superuser",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[(None, '---------'), (True, 'Yes'), (False, 'No')],
        )
    )
    is_active = BooleanFilter(
        field_name="is_active", label="Is Active",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[(None, '---------'), (True, 'Yes'), (False, 'No')],
        )
    )
    is_deleted = BooleanFilter(
        field_name="is_deleted", label="Is Deleted",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[(None, '---------'), (True, 'Yes'), (False, 'No')],
        )
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(),
    )

    class Meta:
        model = UserModel
        fields = [
            'is_verified',
            'is_applicant',
            'is_organization',
            'is_staff',
            'is_admin',
            'is_superuser',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class ApplicantModelFilter(FilterSet):
    user = CharFilter(
        field_name="user", label="User ID",
        widget=TextInput(attrs={'placeholder': 'User ID', 'class': 'form-control'}),
    )
    is_active = BooleanFilter(
        field_name="is_active", label="Is Active",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[(None, '---------'), (True, 'Yes'), (False, 'No')],
        )
    )
    is_deleted = BooleanFilter(
        field_name="is_deleted", label="Is Deleted",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[(None, '---------'), (True, 'Yes'), (False, 'No')],
        )
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(),
    )

    class Meta:
        model = ApplicantModel
        fields = [
            'user',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class OrganizationModelFilter(FilterSet):
    user = CharFilter(
        field_name="user", label="User ID",
        widget=TextInput(attrs={'placeholder': 'User ID', 'class': 'form-control'}),
    )
    is_active = BooleanFilter(
        field_name="is_active", label="Is Active",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[(None, '---------'), (True, 'Yes'), (False, 'No')],
        )
    )
    is_deleted = BooleanFilter(
        field_name="is_deleted", label="Is Deleted",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[(None, '---------'), (True, 'Yes'), (False, 'No')],
        )
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(),
    )

    class Meta:
        model = OrganizationModel
        fields = [
            'user',
            'is_active',
            'is_deleted',
            'created_at',
        ]
