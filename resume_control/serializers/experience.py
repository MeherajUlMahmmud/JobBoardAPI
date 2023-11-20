from rest_framework import serializers

from resume_control.models import *
from resume_control.serializers.resume import ResumeModelSerializer


class ExperienceModelSerializerMeta(serializers.ModelSerializer):
    class Meta:
        model = ExperienceModel
        ref_name = 'ExperienceModelSerializer'
        fields = (
            'uuid',
            'resume',
            'company_name',
            'position',
            'type',
            'start_date',
            'is_current',
            'end_date',
            'description',
            'salary',
            'company_website',
        )


class ExperienceModelSerializer:
    class List(ExperienceModelSerializerMeta):
        resume = ResumeModelSerializer.Lite(read_only=True)

        class Meta(ExperienceModelSerializerMeta.Meta):
            fields = ExperienceModelSerializerMeta.Meta.fields

    class Write(ExperienceModelSerializerMeta):
        class Meta(ExperienceModelSerializerMeta.Meta):
            fields = ExperienceModelSerializerMeta.Meta.fields
