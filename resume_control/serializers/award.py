from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from resume_control.models import *


class AwardModelSerializerMeta(ModelSerializer):
    class Meta:
        model = AwardModel
        ref_name = 'AwardModelSerializer'
        fields = [
            'resume',
            'title',
            'description',
            'link',
            'serial',
        ]


class AwardModelSerializer:
    class List(AwardModelSerializerMeta):
        class Meta(AwardModelSerializerMeta.Meta):
            fields = AwardModelSerializerMeta.Meta.fields + [
                'id',
                'is_active',
                'is_deleted',
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
