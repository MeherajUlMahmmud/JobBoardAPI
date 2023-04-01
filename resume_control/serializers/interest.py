from rest_framework import serializers

from resume_control.models import *


class InterestModelSerializerMeta(serializers.ModelSerializer):
    class Meta:
        model = InterestModel
        fields = ('uuid', 'resume', 'interest', 'description')


class InterestModelSerializer:
    class List(InterestModelSerializerMeta):
        class Meta(InterestModelSerializerMeta.Meta):
            fields = InterestModelSerializerMeta.Meta.fields

    class Write(InterestModelSerializerMeta):
        class Meta(InterestModelSerializerMeta.Meta):
            fields = InterestModelSerializerMeta.Meta.fields
