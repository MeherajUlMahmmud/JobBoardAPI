from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from resume_control.models import *
from user_control.serializers.user import UserModelSerializer


class ReferenceModelSerializerMeta(ModelSerializer):
    class Meta:
        model = ReferenceModel
        fields = [
            'resume',
            'name',
            'email',
            'phone',
            'company_name',
            'position',
            'description',
            'portfolio'
        ]


class ReferenceModelSerializer:
    class List(ReferenceModelSerializerMeta):
        created_by = UserModelSerializer.Lite(read_only=True)
        updated_by = UserModelSerializer.Lite(read_only=True)

        class Meta(ReferenceModelSerializerMeta.Meta):
            fields = ReferenceModelSerializerMeta.Meta.fields + [
                'id',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Write(ReferenceModelSerializerMeta):
        name = CharField(max_length=255, required=True)

        class Meta(ReferenceModelSerializerMeta.Meta):
            fields = ReferenceModelSerializerMeta.Meta.fields

        def validate(self, attrs):
            if attrs['resume'].user.id != self.context['request'].user.id:
                raise ValidationError('You are not allowed to create award for this resume.')
            return attrs
