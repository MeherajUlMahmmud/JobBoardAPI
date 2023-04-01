from rest_framework import serializers

from resume_control.models import *


class ReferenceModelSerializerMeta(serializers.ModelSerializer):
    class Meta:
        model = ReferenceModel
        fields = ('uuid', 'user', 'title', 'description', 'link', 'is_active')


class ReferenceModelSerializer:
    class List(ReferenceModelSerializerMeta):
        class Meta(ReferenceModelSerializerMeta.Meta):
            fields = ReferenceModelSerializerMeta.Meta.fields

    class Write(ReferenceModelSerializerMeta):
        class Meta(ReferenceModelSerializerMeta.Meta):
            fields = ReferenceModelSerializerMeta.Meta.fields
