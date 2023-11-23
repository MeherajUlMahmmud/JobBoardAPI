from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import ModelSerializer

from user_control.serializers.user import UserModelSerializer
from test_control.models import QuestionModel
from test_control.serializers.option import OptionModelSerializer


class QuestionModelSerializerMeta(ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = [
            'exam',
            'type',
            'prompt',
            'is_marked',
            'marks',
        ]


class QuestionModelSerializer:
    class List(QuestionModelSerializerMeta):
        total_options = IntegerField()
        created_by = UserModelSerializer.Lite()
        updated_by = UserModelSerializer.Lite()

        class Meta(QuestionModelSerializerMeta.Meta):
            fields = QuestionModelSerializerMeta.Meta.fields + [
                'id',
                'total_options',
                'options',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class ListForExamine(QuestionModelSerializerMeta):
        class Meta(QuestionModelSerializerMeta.Meta):
            fields = [
                'id',
                'exam',
                'type',
                'prompt',
            ]

    class Details(QuestionModelSerializerMeta):
        options = OptionModelSerializer.List(many=True, allow_null=True)
        created_by = UserModelSerializer.Lite()
        updated_by = UserModelSerializer.Lite()

        class Meta(QuestionModelSerializerMeta.Meta):
            fields = QuestionModelSerializerMeta.Meta.fields + [
                'id',
                'options',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class DetailsForExamine(QuestionModelSerializerMeta):
        options = OptionModelSerializer.DetailsForExamine(many=True, allow_null=True)

        class Meta(QuestionModelSerializerMeta.Meta):
            fields = [
                'id',
                'exam',
                'type',
                'prompt',
                'options',
                'is_marked',
                'marks',
            ]

    class Write(QuestionModelSerializerMeta):
        prompt = CharField(required=True)

        class Meta(QuestionModelSerializerMeta.Meta):
            fields = QuestionModelSerializerMeta.Meta.fields

        def validate(self, attrs):
            if attrs['exam'].created_by.id != self.context['request'].user.id:
                raise ValidationError('You are not allowed to create question for this exam.')
            return attrs
