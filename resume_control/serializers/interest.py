from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from resume_control.models import *
from user_control.serializers.user import UserModelSerializer


class InterestModelSerializerMeta(ModelSerializer):
    class Meta:
        model = InterestModel
        fields = [
            'resume',
            'name',
            'description',
        ]


class InterestModelSerializer:
    class List(InterestModelSerializerMeta):
        created_by = UserModelSerializer.Lite(read_only=True)
        updated_by = UserModelSerializer.Lite(read_only=True)

        class Meta(InterestModelSerializerMeta.Meta):
            fields = InterestModelSerializerMeta.Meta.fields + [
                'id',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Write(InterestModelSerializerMeta):
        title = CharField(max_length=255, required=True)

        class Meta(InterestModelSerializerMeta.Meta):
            fields = InterestModelSerializerMeta.Meta.fields

        def validate(self, attrs):
            if attrs['resume'].user.id != self.context['request'].user.id:
                raise ValidationError('You are not allowed to create award for this resume.')
            return attrs
