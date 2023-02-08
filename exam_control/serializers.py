from rest_framework import serializers

from exam_control.models import ExamModel, QuestionModel, OptionModel, ApplicantResponseModel
from user_control.serializers import ApplicantModelSerializer


class ExamModelGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamModel
        fields = ('uuid', 'organization', 'job', 'name', 'description', 'allocated_time', 'total_marks', 'pass_marks')
        depth = 1


class ExamModelPostSerializer(serializers.ModelSerializer):
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


class QuestionModelGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ('uuid', 'exam', 'question', 'marks', 'type', 'options')
        depth = 1


class QuestionModelPostSerializer(serializers.ModelSerializer):
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


class OptionModelGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionModel
        fields = ['uuid', 'option', 'is_correct']
        depth = 1


class OptionModelPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionModel
        fields = ['uuid', 'question', 'option', 'is_correct']

    def create(self, validated_data):
        option = OptionModel.objects.create(
            question=self.validated_data['question'],
            option=self.validated_data['option'],
            is_correct=self.validated_data['is_correct'],
        )
        return option

    def update(self, instance, validated_data):
        instance.option = validated_data.get('option', instance.option)
        instance.is_correct = validated_data.get('is_correct', instance.is_correct)
        instance.save()
        return instance


class ApplicantResponseModelGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicantResponseModel
        fields = ['uuid', 'exam', 'applicant', 'total_marks', 'start_time', 'submission_time', 'is_submitted', 'is_passed', 'is_late']
        depth = 1


class ApplicantResponseModelPostSerializer(serializers.ModelSerializer):

        class Meta:
            model = ApplicantResponseModel
            fields = ['uuid', 'exam', 'applicant', 'total_marks', 'start_time', 'submission_time', 'is_submitted', 'is_passed', 'is_late']

        def create(self, validated_data):
            applicant_response = ApplicantResponseModel.objects.create(
                exam=self.validated_data['exam'],
                applicant=self.validated_data['applicant'],
                start_time=self.validated_data['start_time'] if self.validated_data['start_time'] else None,
            )
            return applicant_response

        def update(self, instance, validated_data, is_applicant):
            if is_applicant:
                instance.submission_time = validated_data.get('submission_time', instance.submission_time)
                instance.is_submitted = validated_data.get('is_submitted', instance.is_submitted)
                instance.is_late = validated_data.get('is_late', instance.is_late)
            else:
                instance.total_marks = validated_data.get('total_marks', instance.total_marks)
                instance.is_passed = validated_data.get('is_passed', instance.is_passed)

            instance.save()
            return instance


class QuestionResponseModelGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionModel
        fields = ['uuid', 'question', 'marks', 'type', 'options', 'applicant_response']
        depth = 1


class QuestionResponseModelPostSerializer(serializers.ModelSerializer):

        class Meta:
            model = QuestionModel
            fields = ['uuid', 'question', 'marks', 'type', 'options', 'applicant_response']

        def create(self, validated_data, is_correct):
            question_response = QuestionModel.objects.create(
                applicant_response=self.validated_data['applicant_response'],
                question=self.validated_data['question'],
                option=self.validated_data['option'] if self.validated_data['option'] else None,
                text_answer=self.validated_data['text_answer'] if self.validated_data['text_answer'] else None,
                obtained_marks=self.validated_data['obtained_marks'] if self.validated_data['obtained_marks'] else None,
                is_correct=is_correct,
            )
            return question_response

        def update(self, instance, validated_data):
            instance.marks = validated_data.get('marks', instance.marks)
            instance.save()
            return instance
