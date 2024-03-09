from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from resume_control.models import *


class InterestModelSerializerMeta(ModelSerializer):
    class Meta:
        model = InterestModel
        ref_name = 'InterestModelSerializer'
        fields = [
            'resume',
            'name',
            'description',
        ]


class InterestModelSerializer:
    class List(InterestModelSerializerMeta):
        class Meta(InterestModelSerializerMeta.Meta):
            fields = InterestModelSerializerMeta.Meta.fields + [
                'id',
                'is_active',
                'is_deleted',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Write(InterestModelSerializerMeta):
        name = CharField(max_length=255, required=True)

        class Meta(InterestModelSerializerMeta.Meta):
            fields = InterestModelSerializerMeta.Meta.fields

        def validate(self, attrs):
            if attrs['resume'].user.id != self.context['request'].user.id:
                raise ValidationError('You are not allowed to create award for this resume.')
            return attrs
