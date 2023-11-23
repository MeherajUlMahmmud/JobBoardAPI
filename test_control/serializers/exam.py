from rest_framework.serializers import ModelSerializer, IntegerField

from user_control.serializers.user import UserModelSerializer
from test_control.models import ExamModel
from test_control.serializers.question import QuestionModelSerializer


class ExamModelSerializerMeta(ModelSerializer):
    class Meta:
        model = ExamModel
        fields = [
            'title',
            'description',
        ]


class ExamModelSerializer:
    class List(ExamModelSerializerMeta):
        total_questions = IntegerField()
        created_by = UserModelSerializer.Lite(read_only=True)
        updated_by = UserModelSerializer.Lite(read_only=True)

        class Meta(ExamModelSerializerMeta.Meta):
            fields = ExamModelSerializerMeta.Meta.fields + [
                'id',
                'total_duration',
                'total_marks',
                'total_questions',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Lite(ExamModelSerializerMeta):
        class Meta(ExamModelSerializerMeta.Meta):
            fields = [
                'id',
                'title',
                'description',
                'total_duration',
                'created_at',
                'updated_at',
            ]

    class Details(ExamModelSerializerMeta):
        total_questions = IntegerField()
        questions = QuestionModelSerializer.Details(many=True)
        created_by = UserModelSerializer.Lite(read_only=True)
        updated_by = UserModelSerializer.Lite(read_only=True)

        class Meta(ExamModelSerializerMeta.Meta):
            fields = ExamModelSerializerMeta.Meta.fields + [
                'id',
                'total_duration',
                'total_marks',
                'total_marks',
                'total_questions',
                'questions',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Write(ExamModelSerializerMeta):
        class Meta(ExamModelSerializerMeta.Meta):
            fields = ExamModelSerializerMeta.Meta.fields

    class DetailsForExamine(ExamModelSerializerMeta):
        total_questions = IntegerField()
        questions = QuestionModelSerializer.DetailsForExamine(many=True)

        class Meta(ExamModelSerializerMeta.Meta):
            fields = ExamModelSerializerMeta.Meta.fields + [
                'id',
                'total_duration',
                'total_marks',
                'total_questions',
                'updated_at',
            ]
