from rest_framework import serializers

from resume_control.models import *


class SkillModelSerializerMeta(serializers.ModelSerializer):
    class Meta:
        model = SkillModel
        fields = (
            'uuid',
            'resume',
            'skill',
            'proficiency',
            'description',
        )


class SkillModelSerializer:
    class List(SkillModelSerializerMeta):
        class Meta(SkillModelSerializerMeta.Meta):
            fields = SkillModelSerializerMeta.Meta.fields

    class Write(SkillModelSerializerMeta):
        class Meta(SkillModelSerializerMeta.Meta):
            fields = SkillModelSerializerMeta.Meta.fields
