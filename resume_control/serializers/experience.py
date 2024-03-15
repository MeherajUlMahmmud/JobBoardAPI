from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from resume_control.models import *


class ExperienceModelSerializerMeta(ModelSerializer):
    class Meta:
        model = ExperienceModel
        ref_name = 'ExperienceModelSerializer'
        fields = [
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
            'serial',
        ]


class ExperienceModelSerializer:
    class List(ExperienceModelSerializerMeta):
        class Meta(ExperienceModelSerializerMeta.Meta):
            fields = ExperienceModelSerializerMeta.Meta.fields + [
                'id',
                'is_active',
                'is_deleted',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Write(ExperienceModelSerializerMeta):
        company_name = CharField(max_length=255, required=True)
        position = CharField(max_length=255, required=True)

        class Meta(ExperienceModelSerializerMeta.Meta):
            fields = ExperienceModelSerializerMeta.Meta.fields

        def validate(self, attrs):
            if attrs['resume'].user.id != self.context['request'].user.id:
                raise ValidationError('You are not allowed to create award for this resume.')
            return attrs
