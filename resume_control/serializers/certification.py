from rest_framework import serializers

from resume_control.models import *


class CertificationModelSerializerMeta(serializers.ModelSerializer):
    class Meta:
        model = CertificationModel
        fields = ('uuid', 'user', 'title', 'description', 'link', 'is_active')


class CertificationModelSerializer:
    class List(CertificationModelSerializerMeta):
        class Meta(CertificationModelSerializerMeta.Meta):
            fields = CertificationModelSerializerMeta.Meta.fields

    class Write(CertificationModelSerializerMeta):
        class Meta(CertificationModelSerializerMeta.Meta):
            fields = CertificationModelSerializerMeta.Meta.fields
