from rest_framework import serializers

from resume_control.models import *


class LanguageModelSerializerMeta(serializers.ModelSerializer):
    class Meta:
        model = LanguageModel
        fields = ('uuid', 'resume', 'language', 'proficiency', 'description')


class LanguageModelSerializer:
    class List(LanguageModelSerializerMeta):
        class Meta(LanguageModelSerializerMeta.Meta):
            fields = LanguageModelSerializerMeta.Meta.fields

    class Write(LanguageModelSerializerMeta):
        class Meta(LanguageModelSerializerMeta.Meta):
            fields = LanguageModelSerializerMeta.Meta.fields
