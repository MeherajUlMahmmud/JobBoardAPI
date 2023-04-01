from rest_framework import serializers

from resume_control.models import *


class ExperienceModelSerializerMeta(serializers.ModelSerializer):
    class Meta:
        model = ExperienceModel
        fields = ('uuid', 'resume', 'company_name', 'position', 'type', 'start_date', 'end_date', 'description')


class ExperienceModelSerializer:
    class List(ExperienceModelSerializerMeta):
        class Meta(ExperienceModelSerializerMeta.Meta):
            fields = ExperienceModelSerializerMeta.Meta.fields

    class Write(ExperienceModelSerializerMeta):
        class Meta(ExperienceModelSerializerMeta.Meta):
            fields = ExperienceModelSerializerMeta.Meta.fields
