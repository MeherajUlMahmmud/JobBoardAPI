from django.forms import Select, TextInput
from django_filters.rest_framework import FilterSet, BooleanFilter, CharFilter, ChoiceFilter, DateFromToRangeFilter

from common.choices import WorkExperienceTypeChoices
from common.custom_widgets import CustomDateRangeFilterWidget
from resume_control.models import ResumeModel, PersonalModel, ContactModel, EducationModel, ExperienceModel, SkillModel, \
    LanguageModel, InterestModel, ReferenceModel, AwardModel, CertificationModel


class ResumeModelFilter(FilterSet):
    user = CharFilter(
        field_name="user", label="User ID",
        widget=TextInput(attrs={'placeholder': 'User ID', 'class': 'form-control'}),
    )
    name = CharFilter(
        field_name="name", label="Resume Name",
        widget=TextInput(attrs={'placeholder': 'Resume Name', 'class': 'form-control'}),
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
            'created_at',
        ]


class PersonalModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
    )

    class Meta:
        model = PersonalModel
        fields = [
            'resume',
        ]


class ContactModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
    )

    class Meta:
        model = ContactModel
        fields = [
            'resume',
        ]


class EducationModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
    )

    class Meta:
        model = EducationModel
        fields = [
            'resume',
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
    )
    end_date = DateFromToRangeFilter(
        field_name="end_date", label="End Date",
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
        ]


class SkillModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
    )

    class Meta:
        model = SkillModel
        fields = [
            'resume',
        ]


class LanguageModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
    )

    class Meta:
        model = LanguageModel
        fields = [
            'resume',
        ]


class InterestModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
    )

    class Meta:
        model = InterestModel
        fields = [
            'resume',
        ]


class ReferenceModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
    )

    class Meta:
        model = ReferenceModel
        fields = [
            'resume',
        ]


class AwardModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
    )

    class Meta:
        model = AwardModel
        fields = [
            'resume',
        ]


class CertificationModelFilter(FilterSet):
    resume = CharFilter(
        field_name="resume", label="Resume ID",
        widget=TextInput(attrs={'placeholder': 'Resume ID', 'class': 'form-control'}),
    )

    class Meta:
        model = CertificationModel
        fields = [
            'resume',
        ]
