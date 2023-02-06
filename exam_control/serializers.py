from rest_framework import serializers

from exam_control.models import ExamModel, QuestionModel, OptionModel, ApplicantResponseModel
from job_control.serializer import JobDetailSerializer
from user_control.serializers import OrganizationModelSerializer, ApplicantModelSerializer


class ExamGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamModel
        fields = ('uuid', 'organization', 'job', 'name', 'description', 'allocated_time', 'total_marks', 'pass_marks')
        depth = 1


class ExamPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamModel
        fields = ('uuid', 'organization', 'job', 'name', 'description', 'allocated_time', 'total_marks', 'pass_marks')

    def create(self, validated_data):
        exam = ExamModel.objects.create(
            organization=self.validated_data['organization'],
            job=self.validated_data['job'],
            name=self.validated_data['name'],
            description=self.validated_data['description'] if self.validated_data['description'] else '',
            allocated_time=self.validated_data['allocated_time'] if self.validated_data['allocated_time'] else 0,
            total_marks=self.validated_data['total_marks'] if self.validated_data['total_marks'] else 0,
            pass_marks=self.validated_data['pass_marks'] if self.validated_data['pass_marks'] else 0,
        )
        return exam

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.allocated_time = validated_data.get('allocated_time', instance.allocated_time)
        instance.total_marks = validated_data.get('total_marks', instance.total_marks)
        instance.pass_marks = validated_data.get('pass_marks', instance.pass_marks)
        instance.save()
        return instance


class QuestionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ('uuid', 'exam', 'question', 'marks', 'type')
        depth = 1


class QuestionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ('uuid', 'exam', 'question', 'marks', 'type')

    def create(self, validated_data):
        question = QuestionModel.objects.create(
            exam=self.validated_data['exam'],
            question=self.validated_data['question'],
            marks=self.validated_data['marks'] if self.validated_data['marks'] else 0,
            type=self.validated_data['type'],
        )
        return question

    def update(self, instance, validated_data):
        instance.question = validated_data.get('question', instance.question)
        instance.marks = validated_data.get('marks', instance.marks)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance


class OptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionModel
        fields = ['uuid', 'option', 'is_correct']
        depth = 1


class OptionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionModel
        fields = ['uuid', 'question', 'option', 'is_correct']

    def save(self, **kwargs):
        option = OptionModel.objects.create(
            question=self.validated_data['question'],
            option=self.validated_data['option'],
            is_correct=self.validated_data['is_correct'],
        )
        # add option to question
        question = self.validated_data['question']
        question.options.add(option)

        return option


class ApplicantResponseDetailSerializer(serializers.ModelSerializer):
    exam = serializers.SerializerMethodField()
    applicant = serializers.SerializerMethodField()

    class Meta:
        model = ApplicantResponseModel
        fields = ['uuid', 'exam', 'applicant', 'total_marks', 'start_time', 'submission_time', 'is_submitted', 'is_passed', 'is_late']

    # def get_exam(self, obj):
    #     return ExamDetailSerializer(obj.exam).data

    def get_applicant(self, obj):
        return ApplicantModelSerializer(obj.applicant).data
