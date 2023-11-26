from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from user_control.serializers.user import UserModelSerializer
from test_control.models import OptionModel


class OptionModelSerializerMeta(ModelSerializer):
    class Meta:
        model = OptionModel
        ref_name = 'OptionModelSerializer'
        fields = [
            'question',
            'text',
        ]


class OptionModelSerializer:
    class List(OptionModelSerializerMeta):
        created_by = UserModelSerializer.Lite()
        updated_by = UserModelSerializer.Lite()

        class Meta(OptionModelSerializerMeta.Meta):
            fields = OptionModelSerializerMeta.Meta.fields + [
                'id',
                'is_correct',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Lite(OptionModelSerializerMeta):
        class Meta(OptionModelSerializerMeta.Meta):
            fields = OptionModelSerializerMeta.Meta.fields + [
                'id',
                'is_correct',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class DetailsForExamine(OptionModelSerializerMeta):
        class Meta(OptionModelSerializerMeta.Meta):
            fields = OptionModelSerializerMeta.Meta.fields + [
                'id',
                'updated_at',
            ]

    class Write(OptionModelSerializerMeta):
        text = CharField(required=True)

        class Meta(OptionModelSerializerMeta.Meta):
            fields = OptionModelSerializerMeta.Meta.fields + [
                'is_correct',
            ]
