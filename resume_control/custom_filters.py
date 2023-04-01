from django_filters.rest_framework import FilterSet, CharFilter, DateFromToRangeFilter

from common.custom_widgets import CustomDateRangeFilterWidget
from resume_control.models import ResumeModel, PersonalModel, ContactModel, EducationModel, ExperienceModel, SkillModel, \
    LanguageModel, InterestModel, ReferenceModel, AwardModel, CertificationModel


class ResumeModelFilter(FilterSet):
    user = CharFilter(field_name="user", label="User ID")
    name = CharFilter(field_name="name", label="Resume Name")
    created_at = DateFromToRangeFilter(field_name="created_at", label="Created At",
                                       widget=CustomDateRangeFilterWidget())

    class Meta:
        model = ResumeModel
        fields = [
            'user',
            'name',
            'created_at',
        ]


class PersonalModelFilter(FilterSet):
    resume = CharFilter(field_name="resume", label="Resume ID")

    class Meta:
        model = PersonalModel
        fields = [
            'resume',
        ]


class ContactModelFilter(FilterSet):
    resume = CharFilter(field_name="resume", label="Resume ID")

    class Meta:
        model = ContactModel
        fields = [
            'resume',
        ]


class EducationModelFilter(FilterSet):
    resume = CharFilter(field_name="resume", label="Resume ID")

    class Meta:
        model = EducationModel
        fields = [
            'resume',
        ]


class ExperienceModelFilter(FilterSet):
    resume = CharFilter(field_name="resume", label="Resume ID")

    class Meta:
        model = ExperienceModel
        fields = [
            'resume',
        ]


class SkillModelFilter(FilterSet):
    resume = CharFilter(field_name="resume", label="Resume ID")

    class Meta:
        model = SkillModel
        fields = [
            'resume',
        ]


class LanguageModelFilter(FilterSet):
    resume = CharFilter(field_name="resume", label="Resume ID")

    class Meta:
        model = LanguageModel
        fields = [
            'resume',
        ]


class InterestModelFilter(FilterSet):
    resume = CharFilter(field_name="resume", label="Resume ID")

    class Meta:
        model = InterestModel
        fields = [
            'resume',
        ]


class ReferenceModelFilter(FilterSet):
    resume = CharFilter(field_name="resume", label="Resume ID")

    class Meta:
        model = ReferenceModel
        fields = [
            'resume',
        ]


class AwardModelFilter(FilterSet):
    resume = CharFilter(field_name="resume", label="Resume ID")

    class Meta:
        model = AwardModel
        fields = [
            'resume',
        ]


class CertificationModelFilter(FilterSet):
    resume = CharFilter(field_name="resume", label="Resume ID")

    class Meta:
        model = CertificationModel
        fields = [
            'resume',
        ]
