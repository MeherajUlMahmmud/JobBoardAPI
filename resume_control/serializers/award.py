from rest_framework.serializers import ModelSerializer

from resume_control.models import *


class AwardModelSerializerMeta(ModelSerializer):
    class Meta:
        model = AwardModel
        fields = ('uuid', 'user', 'title', 'description', 'link', 'is_active')


class AwardModelSerializer:
    class List(AwardModelSerializerMeta):
        class Meta(AwardModelSerializerMeta.Meta):
            fields = AwardModelSerializerMeta.Meta.fields

    class Write(AwardModelSerializerMeta):
        class Meta(AwardModelSerializerMeta.Meta):
            fields = AwardModelSerializerMeta.Meta.fields
