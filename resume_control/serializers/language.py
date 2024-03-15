from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from resume_control.models import *


class LanguageModelSerializerMeta(ModelSerializer):
    class Meta:
        model = LanguageModel
        ref_name = 'LanguageModelSerializer'
        fields = [
            'resume',
            'name',
            'proficiency',
            'description',
            'serial',
        ]


class LanguageModelSerializer:
    class List(LanguageModelSerializerMeta):
        class Meta(LanguageModelSerializerMeta.Meta):
            fields = LanguageModelSerializerMeta.Meta.fields + [
                'id',
                'is_active',
                'is_deleted',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Write(LanguageModelSerializerMeta):
        name = CharField(max_length=255, required=True)

        class Meta(LanguageModelSerializerMeta.Meta):
            fields = LanguageModelSerializerMeta.Meta.fields

        def validate(self, attrs):
            if attrs['resume'].user.id != self.context['request'].user.id:
                raise ValidationError('You are not allowed to create or update language for this resume.')
            return attrs
