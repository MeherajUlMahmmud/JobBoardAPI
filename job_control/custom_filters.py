from django.forms import Select, TextInput
from django_filters.rest_framework import (
    FilterSet, BooleanFilter, CharFilter, ChoiceFilter, DateFromToRangeFilter,
)

from common.choices import YesNoChoices
from common.custom_widgets import CustomDateRangeFilterWidget
from job_control.models import JobTypeModel, JobModel


class JobTypeModelFilter(FilterSet):
    name = CharFilter(
        field_name="name", label="Job Type Name",
        widget=TextInput(attrs={'placeholder': 'Job Type Name', 'class': 'form-control'}),
    )
    is_active = BooleanFilter(
        field_name="is_active", label="Is Active",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[YesNoChoices],
        )
    )
    is_deleted = BooleanFilter(
        field_name="is_deleted", label="Is Deleted",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[YesNoChoices],
        )
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(),
    )

    class Meta:
        model = JobTypeModel
        fields = [
            'name',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class JobModelFilter(FilterSet):
    organization = CharFilter(
        field_name="resume", label="Organization ID",
        widget=TextInput(attrs={'placeholder': 'Organization ID', 'class': 'form-control'}),
    )
    title = CharFilter(
        field_name="title", label="Job Title",
        widget=TextInput(attrs={'placeholder': 'Job Title', 'class': 'form-control'}),
    )
    department = CharFilter(
        field_name="department", label="Department",
        widget=TextInput(attrs={'placeholder': 'Department', 'class': 'form-control'}),
    )
    location = CharFilter(
        field_name="location", label="Location",
        widget=TextInput(attrs={'placeholder': 'Location', 'class': 'form-control'}),
    )
    job_types = CharFilter(
        field_name="job_types", label="Job Types",
        widget=TextInput(attrs={'placeholder': 'Job Types', 'class': 'form-control'}),
    )
    is_fixed_salary = BooleanFilter(
        field_name="is_fixed_salary", label="Is Fixed Salary",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[YesNoChoices],
        )
    )
    salary = CharFilter(
        field_name="salary", label="Salary",
        widget=TextInput(attrs={'placeholder': 'Salary', 'class': 'form-control'}),
    )
    total_vacancy = CharFilter(
        field_name="total_vacancy", label="Total Vacancy",
        widget=TextInput(attrs={'placeholder': 'Total Vacancy', 'class': 'form-control'}),
    )
    is_active = BooleanFilter(
        field_name="is_active", label="Is Active",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[YesNoChoices],
        )
    )
    is_deleted = BooleanFilter(
        field_name="is_deleted", label="Is Deleted",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[YesNoChoices],
        )
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(),
    )

    class Meta:
        model = JobModel
        fields = [
            'organization',
            'title',
            'department',
            'location',
            'job_types',
            'is_fixed_salary',
            'salary',
            'total_vacancy',
            'is_active',
            'is_deleted',
            'created_at',
        ]
