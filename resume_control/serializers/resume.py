from rest_framework.serializers import ModelSerializer

from resume_control.models import ResumeModel
from resume_control.serializers.award import AwardModelSerializer
from resume_control.serializers.certification import CertificationModelSerializer
from resume_control.serializers.contact import ContactModelSerializer
from resume_control.serializers.education import EducationModelSerializer
from resume_control.serializers.experience import ExperienceModelSerializer
from resume_control.serializers.interest import InterestModelSerializer
from resume_control.serializers.language import LanguageModelSerializer
from resume_control.serializers.personal import PersonalModelSerializer
from resume_control.serializers.reference import ReferenceModelSerializer
from resume_control.serializers.skill import SkillModelSerializer
from user_control.serializers.user import UserModelSerializer


class ResumeModelSerializerMeta(ModelSerializer):
    class Meta:
        model = ResumeModel
        ref_name = 'ResumeModelSerializer'
        fields = [
            'name',
        ]


class ResumeModelSerializer(ResumeModelSerializerMeta):
    class List(ResumeModelSerializerMeta):
        user = UserModelSerializer.Lite()

        class Meta(ResumeModelSerializerMeta.Meta):
            fields = ResumeModelSerializerMeta.Meta.fields + [
                'id',
                'user',
                'is_education_visible',
                'is_experience_visible',
                'is_skill_visible',
                'is_language_visible',
                'is_interest_visible',
                'is_reference_visible',
                'is_award_visible',
                'is_certification_visible',
                'is_active',
                'is_deleted',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Lite(ResumeModelSerializerMeta):
        class Meta(ResumeModelSerializerMeta.Meta):
            fields = ResumeModelSerializerMeta.Meta.fields + [
                'id',
                'created_at',
                'updated_at',
            ]

    class Preview(ResumeModelSerializerMeta):
        user = UserModelSerializer.Lite()
        personal = PersonalModelSerializer.List()
        contact = ContactModelSerializer.List()
        education = EducationModelSerializer.List(many=True)
        experience = ExperienceModelSerializer.List(many=True)
        skill = SkillModelSerializer.List(many=True)
        language = LanguageModelSerializer.List(many=True)
        interest = InterestModelSerializer.List(many=True)
        reference = ReferenceModelSerializer.List(many=True)
        award = AwardModelSerializer.List(many=True)
        certification = CertificationModelSerializer.List(many=True)

        class Meta(ResumeModelSerializerMeta.Meta):
            fields = ResumeModelSerializerMeta.Meta.fields + [
                'id',
                'user',
                'personal',
                'contact',
                'education',
                'experience',
                'skill',
                'language',
                'interest',
                'reference',
                'award',
                'certification',
                'is_education_visible',
                'is_experience_visible',
                'is_skill_visible',
                'is_language_visible',
                'is_interest_visible',
                'is_reference_visible',
                'is_award_visible',
                'is_certification_visible',
                'is_active',
                'is_deleted',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',

            ]

    class Write(ResumeModelSerializerMeta):
        class Meta(ResumeModelSerializerMeta.Meta):
            fields = ResumeModelSerializerMeta.Meta.fields
