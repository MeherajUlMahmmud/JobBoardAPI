from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from resume_control.models import *
from user_control.serializers.user import UserModelSerializer


class AwardModelSerializerMeta(ModelSerializer):
    class Meta:
        model = AwardModel
        ref_name = 'AwardModelSerializer'
        fields = [
            'resume',
            'title',
            'description',
            'link',
        ]


class AwardModelSerializer:
    class List(AwardModelSerializerMeta):
        created_by = UserModelSerializer.Lite(read_only=True)
        updated_by = UserModelSerializer.Lite(read_only=True)

        class Meta(AwardModelSerializerMeta.Meta):
            fields = AwardModelSerializerMeta.Meta.fields + [
                'id',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Write(AwardModelSerializerMeta):
        title = CharField(max_length=255, required=True)

        class Meta(AwardModelSerializerMeta.Meta):
            fields = AwardModelSerializerMeta.Meta.fields

        def validate(self, attrs):
            if attrs['resume'].user.id != self.context['request'].user.id:
                raise ValidationError('You are not allowed to create award for this resume.')
            return attrs
