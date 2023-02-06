from rest_framework import serializers

from exam_control.models import ExamModel, QuestionModel, OptionModel, ApplicantResponseModel
from job_control.serializer import JobDetailSerializer
from user_control.serializers import OrganizationModelSerializer, ApplicantModelSerializer


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamModel
        # fields = '__all__'
        fields = ('uuid', 'job', 'name', 'description', 'allocated_time', 'total_marks', 'pass_marks')
        depth = 1  # This is the magic line that will allow us to get the related data


class ExamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamModel
        fields = ('uuid', 'organization', 'job', 'name', 'description', 'allocated_time', 'total_marks', 'pass_marks')

    def save(self, **kwargs):
        exam = ExamModel.objects.create(
            organization=self.validated_data['organization'],
            job=self.validated_data['job'],
            name=self.validated_data['name'],
            description=self.validated_data['description'],
            allocated_time=self.validated_data['allocated_time'],
            # total_marks=self.validated_data['total_marks'],
            pass_marks=self.validated_data['pass_marks'],
        )
        return exam


class ExamDetailSerializer(serializers.ModelSerializer):
    organization = serializers.SerializerMethodField()
    job = serializers.SerializerMethodField()

    class Meta:
        model = ExamModel
        fields = '__all__'
        depth = 1  # This is the magic line that will allow us to get the related data

    def get_organization(self, obj):
        return OrganizationModelSerializer(obj.organization).data

    def get_job(self, obj):
        return JobDetailSerializer(obj.job).data


class QuestionSerializer(serializers.ModelSerializer):
    pass


class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ('uuid', 'exam', 'question', 'marks', 'type')

    def save(self, **kwargs):
        question = QuestionModel.objects.create(
            exam=self.validated_data['exam'],
            question=self.validated_data['question'],
            type=self.validated_data['type'],
            marks=self.validated_data['marks'],
        )
        return question


class QuestionDetailSerializer(serializers.ModelSerializer):
    exam = serializers.SerializerMethodField()
    options = serializers.SerializerMethodField()

    class Meta:
        model = QuestionModel
        fields = ['uuid', 'question', 'exam', 'options', 'type', 'marks']

    def get_exam(self, obj):
        return ExamSerializer(obj.exam).data

    def get_options(self, obj):
        return OptionModelSerializer(obj.options, many=True).data


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

    def get_exam(self, obj):
        return ExamDetailSerializer(obj.exam).data

    def get_applicant(self, obj):
        return ApplicantModelSerializer(obj.applicant).data
