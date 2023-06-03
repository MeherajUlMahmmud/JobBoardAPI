from rest_framework import serializers

from resume_control.models import *


class ReferenceModelSerializerMeta(serializers.ModelSerializer):
    class Meta:
        model = ReferenceModel
        fields = (
            'uuid',
            'resume',
            'name',
            'email',
            'phone',
            'company_name',
            'position',
            'description',
        )


class ReferenceModelSerializer:
    class List(ReferenceModelSerializerMeta):
        class Meta(ReferenceModelSerializerMeta.Meta):
            fields = ReferenceModelSerializerMeta.Meta.fields

    class Write(ReferenceModelSerializerMeta):
        class Meta(ReferenceModelSerializerMeta.Meta):
            fields = ReferenceModelSerializerMeta.Meta.fields
