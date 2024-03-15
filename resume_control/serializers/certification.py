from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from resume_control.models import *


class CertificationModelSerializerMeta(ModelSerializer):
    class Meta:
        model = CertificationModel
        ref_name = 'CertificationModelSerializer'
        fields = [
            'resume',
            'title',
            'description',
            'link',
            'start_date',
            'end_date',
            'serial',
        ]


class CertificationModelSerializer:
    class List(CertificationModelSerializerMeta):
        class Meta(CertificationModelSerializerMeta.Meta):
            fields = CertificationModelSerializerMeta.Meta.fields + [
                'id',
                'is_active',
                'is_deleted',
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
