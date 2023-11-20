from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from resume_control.models import *
from user_control.serializers.user import UserModelSerializer


class CertificationModelSerializerMeta(ModelSerializer):
    class Meta:
        model = CertificationModel
        ref_name = 'CertificationModelSerializer'
        fields = [
            'title',
            'description',
            'link',
            'start_date',
            'end_date',
        ]


class CertificationModelSerializer:
    class List(CertificationModelSerializerMeta):
        created_by = UserModelSerializer.Lite(read_only=True)
        updated_by = UserModelSerializer.Lite(read_only=True)

        class Meta(CertificationModelSerializerMeta.Meta):
            fields = CertificationModelSerializerMeta.Meta.fields + [
                'id',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Write(CertificationModelSerializerMeta):
        title = CharField(max_length=255, required=True)

        class Meta(CertificationModelSerializerMeta.Meta):
            fields = CertificationModelSerializerMeta.Meta.fields

        def validate(self, attrs):
            if attrs['resume'].user.id != self.context['request'].user.id:
                raise ValidationError('You are not allowed to create award for this resume.')
            return attrs
