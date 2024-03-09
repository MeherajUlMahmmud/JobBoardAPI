from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from resume_control.models import *


class SkillModelSerializerMeta(ModelSerializer):
    class Meta:
        model = SkillModel
        ref_name = 'SkillModelSerializer'
        fields = [
            'resume',
            'name',
            'proficiency',
            'description',
        ]


class SkillModelSerializer:
    class List(SkillModelSerializerMeta):
        class Meta(SkillModelSerializerMeta.Meta):
            fields = SkillModelSerializerMeta.Meta.fields + [
                'id',
                'is_active',
                'is_deleted',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Write(SkillModelSerializerMeta):
        name = CharField(max_length=255, required=True)

        class Meta(SkillModelSerializerMeta.Meta):
            fields = SkillModelSerializerMeta.Meta.fields

        def validate(self, attrs):
            if attrs['resume'].user.id != self.context['request'].user.id:
                raise ValidationError('You are not allowed to create or update skill for this resume.')
            return attrs
