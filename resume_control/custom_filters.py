from django.forms import Select, TextInput
from django_filters.rest_framework import (
    FilterSet, BooleanFilter, CharFilter, ChoiceFilter, DateFromToRangeFilter,
)

from common.choices import WorkExperienceTypeChoices, YesNoChoices
from common.custom_widgets import CustomDateRangeFilterWidget
from resume_control.models import (
    ResumeModel, PersonalModel, ContactModel, EducationModel, ExperienceModel, SkillModel, LanguageModel, InterestModel,
    ReferenceModel, AwardModel, CertificationModel,
)


class ResumeModelFilter(FilterSet):
    user = CharFilter(
        field_name="user", label="User ID",
        widget=TextInput(attrs={'placeholder': 'User ID', 'class': 'form-control'}),
    )
    name = CharFilter(
        field_name="name", label="Resume Name",
        widget=TextInput(attrs={'placeholder': 'Resume Name', 'class': 'form-control'}),
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
        model = ResumeModel
        fields = [
            'user',
            'name',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class PersonalModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
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
        model = PersonalModel
        fields = [
            'resume',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class ContactModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
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
        model = ContactModel
        fields = [
            'resume',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class EducationModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
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
        model = EducationModel
        fields = [
            'resume',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class ExperienceModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
    )
    type = ChoiceFilter(
        field_name="type", label="Type",
        choices=WorkExperienceTypeChoices.choices,
        widget=Select(attrs={'class': 'form-control'}),
    )
    start_date = DateFromToRangeFilter(
        field_name="start_date", label="Start Date",
        widget=CustomDateRangeFilterWidget(),
    )
    is_current = BooleanFilter(
        field_name="is_current", label="Is Current",
        widget=Select(
            attrs={'class': 'form-control'},
            choices=[YesNoChoices],
        )
    )
    end_date = DateFromToRangeFilter(
        field_name="end_date", label="End Date",
        widget=CustomDateRangeFilterWidget(),
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
        model = ExperienceModel
        fields = [
            'resume',
            'type',
            'start_date',
            'is_current',
            'end_date',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class SkillModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
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
        model = SkillModel
        fields = [
            'resume',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class LanguageModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
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
        model = LanguageModel
        fields = [
            'resume',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class InterestModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
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
        model = InterestModel
        fields = [
            'resume',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class ReferenceModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
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
        model = ReferenceModel
        fields = [
            'resume',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class AwardModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
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
        model = AwardModel
        fields = [
            'resume',
            'is_active',
            'is_deleted',
            'created_at',
        ]


class CertificationModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
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
        model = CertificationModel
        fields = [
            'resume',
            'is_active',
            'is_deleted',
            'created_at',
        ]
