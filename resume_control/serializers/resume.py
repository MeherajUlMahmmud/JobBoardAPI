from rest_framework.serializers import ModelSerializer

from resume_control.models import ResumeModel
from resume_control.serializers.contact import ContactModelSerializer
from resume_control.serializers.personal import PersonalModelSerializer
from user_control.serializers.user import UserModelSerializer


class ResumeModelSerializerMeta(ModelSerializer):
    class Meta:
        model = ResumeModel
        fields = [
            'user',
            'name',
        ]


class ResumeModelSerializer(ResumeModelSerializerMeta):
    class List(ResumeModelSerializerMeta):
        user = UserModelSerializer.Lite()

        class Meta(ResumeModelSerializerMeta.Meta):
            fields = ResumeModelSerializerMeta.Meta.fields + [
                'id',
                'is_education_visible',
                'is_experience_visible',
                'is_skill_visible',
                'is_language_visible',
                'is_interest_visible',
                'is_reference_visible',
                'is_award_visible',
                'is_certification_visible',
                'created_at',
                'updated_at',
            ]

    class Lite(ResumeModelSerializerMeta):
        class Meta(ResumeModelSerializerMeta.Meta):
            fields = ResumeModelSerializerMeta.Meta.fields + [
                'id',
                'created_at',
                'updated_at',
            ]

    class Detail(ResumeModelSerializerMeta):
        user = UserModelSerializer.List()
        personal = PersonalModelSerializer()
        contact = ContactModelSerializer()

        class Meta(ResumeModelSerializerMeta.Meta):
            fields = ResumeModelSerializerMeta.Meta.fields + [
                'uuid', 'personal', 'contact', 'created_at', 'updated_at',
            ]

    class Write(ResumeModelSerializerMeta):
        class Meta(ResumeModelSerializerMeta.Meta):
            fields = ResumeModelSerializerMeta.Meta.fields
