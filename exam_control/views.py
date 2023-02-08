from datetime import datetime

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED


from exam_control.models import ExamModel, QuestionModel, ApplicantResponseModel, OptionModel, QuestionResponseModel
from exam_control.serializers import ExamModelGetSerializer, ExamModelPostSerializer, QuestionModelGetSerializer, \
    QuestionModelPostSerializer, OptionModelGetSerializer, OptionModelPostSerializer, \
    ApplicantResponseModelGetSerializer, ApplicantResponseModelPostSerializer, QuestionResponseModelGetSerializer, \
    QuestionResponseModelPostSerializer
from job_control.models import JobModel, JobApplicationModel
from user_control.models import ApplicantModel


class ExamAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        job_id = request.GET.get('job_id')
        exam_id = request.GET.get('exam_id')
        if request.user.is_organization:
            if job_id and exam_id:
                exam = ExamModel.objects.get(uuid=exam_id, job__uuid=job_id)
                if exam:
                    exam_serializer = ExamModelGetSerializer(exam)
                    return Response(exam_serializer.data, status=HTTP_200_OK)
                else:
                    return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
            elif job_id:
                job = JobModel.objects.get(uuid=job_id)
                if job:
                    exams = ExamModel.objects.filter(job=job)
                    exam_serializer = ExamModelGetSerializer(exams, many=True)
                    return Response(exam_serializer.data, status=HTTP_200_OK)
                else:
                    return Response({'error': 'Job does not exist'}, status=HTTP_400_BAD_REQUEST)
            elif exam_id:
                exam = ExamModel.objects.get(uuid=exam_id)
                if exam:
                    exam_serializer = ExamModelGetSerializer(exam)
                    return Response(exam_serializer.data, status=HTTP_200_OK)
                else:
                    return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Job or Exam id is required'}, status=HTTP_400_BAD_REQUEST)
        elif request.user.is_applicant:
            if job_id and exam_id:
                exam = ExamModel.objects.get(uuid=exam_id, job__uuid=job_id)
                if exam:
                    exam_serializer = ExamModelGetSerializer(exam)
                    applicant_response = ApplicantResponseModel.objects.get(exam=exam, applicant=request.user.applicant)
                    applicant_response_serializer = ApplicantResponseModelGetSerializer(applicant_response)
                    return Response({'exam': exam_serializer.data, 'applicant_response': applicant_response_serializer.data}, status=HTTP_200_OK)
                else:
                    return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
            elif job_id:
                job = JobModel.objects.get(uuid=job_id)
                if job:
                    exams = ExamModel.objects.filter(job=job)
                    exam_serializer = ExamModelGetSerializer(exams, many=True)
                    return Response(exam_serializer.data, status=HTTP_200_OK)
                else:
                    return Response({'error': 'Job does not exist'}, status=HTTP_400_BAD_REQUEST)
            elif exam_id:
                exam = ExamModel.objects.get(uuid=exam_id)
                if exam:
                    exam_serializer = ExamModelGetSerializer(exam)
                    return Response(exam_serializer.data, status=HTTP_200_OK)
                else:
                    return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Job or Exam id is required'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not authenticated'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        job_id = request.data.get('job_id')
        if request.user.is_organization:
            organization = request.user.organization
            job = JobModel.objects.get(uuid=job_id, organization=organization)
            if job:
                exam_serializer = ExamModelPostSerializer(data={
                    'organization': organization.uuid,
                    'job': job_id,
                    'name': request.data.get('name'),
                    'description': request.data.get('description'),
                    'allocated_time': request.data.get('allocated_time'),
                    'total_marks': request.data.get('total_marks'),
                    'pass_marks': request.data.get('pass_marks'),
                })
                if exam_serializer.is_valid():
                    exam = exam_serializer.create(exam_serializer.validated_data)
                    exam_serializer_data = ExamModelGetSerializer(exam).data
                    return Response(exam_serializer_data, status=HTTP_201_CREATED)
                else:
                    return Response(exam_serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Job does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request):
        exam_id = request.GET.get('exam_id')
        if request.user.is_organization:
            exam = ExamModel.objects.get(uuid=exam_id, organization=request.user.organization)
            if exam:
                exam_serializer = ExamModelPostSerializer(exam, data={
                    'job': exam.job.uuid,
                    'organization': request.user.organization.uuid,
                    'name': request.data.get('name'),
                    'description': request.data.get('description'),
                    'allocated_time': request.data.get('allocated_time'),
                    'pass_marks': request.data.get('pass_marks'),
                })
                if exam_serializer.is_valid():
                    exam = exam_serializer.update(exam, exam_serializer.validated_data)
                    exam_serializer_data = ExamModelGetSerializer(exam).data
                    return Response(exam_serializer_data, status=HTTP_201_CREATED)
                else:
                    return Response(exam_serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        exam_id = request.GET.get('exam_id')
        if request.user.is_organization:
            exam = ExamModel.objects.get(uuid=exam_id, organization=request.user.organization)
            if exam:
                exam.delete()
                return Response({'success': 'Exam deleted successfully'}, status=HTTP_200_OK)
            else:
                return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)


class QuestionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        exam_id = request.GET.get('exam_id')
        question_id = request.GET.get('question_id')
        if exam_id and question_id:
            question = QuestionModel.objects.get(uuid=question_id, exam__uuid=exam_id)
            if question:
                question_serializer_data = QuestionModelGetSerializer(question).data
                return Response(question_serializer_data, status=HTTP_200_OK)
            else:
                return Response({'error': 'Question does not exist'}, status=HTTP_400_BAD_REQUEST)
        elif exam_id:
            exam = ExamModel.objects.get(uuid=exam_id)
            if exam:
                questions = QuestionModel.objects.filter(exam=exam)
                question_serializer_data = QuestionModelGetSerializer(questions, many=True).data
                return Response(question_serializer_data, status=HTTP_200_OK)
            else:
                return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
        elif question_id:
            question = QuestionModel.objects.get(uuid=question_id)
            if question:
                question_serializer_data = QuestionModelGetSerializer(question).data
                return Response(question_serializer_data, status=HTTP_200_OK)
            else:
                return Response({'error': 'Question does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No exam or question id provided'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        exam_id = request.data.get('exam_id')
        if request.user.is_organization:
            exam = ExamModel.objects.get(uuid=exam_id, is_active=True, is_deleted=False)
            if exam:
                question_serializer = QuestionModelPostSerializer(data={
                    'exam': exam_id,
                    'question': request.data.get('question'),
                    'type': request.data.get('type'),
                    'marks': request.data.get('marks'),
                })
                if question_serializer.is_valid():
                    question = question_serializer.create(question_serializer.validated_data)
                    question_serializer_data = QuestionModelGetSerializer(question).data
                    return Response(question_serializer_data, status=HTTP_201_CREATED)
                else:
                    return Response(question_serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request):
        question_id = request.GET.get('question_id')
        if request.user.is_organization:
            question = QuestionModel.objects.get(uuid=question_id)
            if question:
                question_serializer = QuestionModelPostSerializer(question, data={
                    'exam': question.exam.uuid,
                    'question': request.data.get('question'),
                    'type': request.data.get('type'),
                    'marks': request.data.get('marks'),
                })
                if question_serializer.is_valid():
                    question = question_serializer.update(question, question_serializer.validated_data)
                    question_serializer_data = QuestionModelGetSerializer(question).data
                    return Response(question_serializer_data, status=HTTP_201_CREATED)
                else:
                    return Response(question_serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Question does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        question_id = request.GET.get('question_id')
        if request.user.is_organization:
            question = QuestionModel.objects.get(uuid=question_id)
            if question:
                question.delete()
                return Response({'success': 'Question deleted successfully'}, status=HTTP_200_OK)
            else:
                return Response({'error': 'Question does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)


class OptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        question_id = request.GET.get('question_id')
        question = QuestionModel.objects.get(uuid=question_id)
        if question:
            options = OptionModel.objects.filter(question=question)
            option_serializer_data = OptionModelGetSerializer(options, many=True).data
            return Response(option_serializer_data, status=HTTP_200_OK)
        else:
            return Response({'error': 'Question does not exist'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        question_id = request.data.get('question_id')
        if request.user.is_organization:
            question = QuestionModel.objects.get(uuid=question_id)
            if question:
                option_serializer = OptionModelPostSerializer(data={
                    'question': question_id,
                    'option': request.data.get('option'),
                    'is_correct': request.data.get('is_correct'),
                })
                if option_serializer.is_valid():
                    option = option_serializer.create(option_serializer.validated_data)
                    option_serializer_data = OptionModelGetSerializer(option).data
                    return Response(option_serializer_data, status=HTTP_201_CREATED)
                else:
                    return Response(option_serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Question does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request):
        option_id = request.GET.get('option_id')
        if request.user.is_organization:
            option = OptionModel.objects.get(uuid=option_id)
            if option:
                option_serializer = OptionModelPostSerializer(option, data={
                    'question': option.question.uuid,
                    'option': request.data.get('option'),
                    'is_correct': request.data.get('is_correct'),
                })
                if option_serializer.is_valid():
                    option = option_serializer.update(option, option_serializer.validated_data)
                    option_serializer_data = OptionModelGetSerializer(option).data
                    return Response(option_serializer_data, status=HTTP_201_CREATED)
                else:
                    return Response(option_serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Option does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        option_id = request.GET.get('option_id')
        if request.user.is_organization:
            option = OptionModel.objects.get(uuid=option_id)
            if option:
                option.delete()
                return Response({'success': 'Option deleted successfully'}, status=HTTP_200_OK)
            else:
                return Response({'error': 'Option does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)


class ApplicantResponseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        exam_id = request.GET.get('exam_id')
        response_id = request.GET.get('response_id')
        if request.user.is_organization:
            if response_id:
                applicant_response = ApplicantResponseModel.objects.get(uuid=response_id)
                if applicant_response:
                    applicant_response_serializer_data = ApplicantResponseModelGetSerializer(applicant_response).data
                    return Response(applicant_response_serializer_data, status=HTTP_200_OK)
            elif exam_id:
                exam = ExamModel.objects.get(uuid=exam_id)
                if exam:
                    applicant_responses = ApplicantResponseModel.objects.filter(exam=exam)
                    applicant_response_serializer_data = ApplicantResponseModelGetSerializer(applicant_responses, many=True).data
                    return Response(applicant_response_serializer_data, status=HTTP_200_OK)
                else:
                    return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
            else:
                applicant_responses = ApplicantResponseModel.objects.all()
                applicant_response_serializer_data = ApplicantResponseModelGetSerializer(applicant_responses, many=True).data
                return Response(applicant_response_serializer_data, status=HTTP_200_OK)
        elif request.user.is_applicant:
            if exam_id:
                exam = ExamModel.objects.get(uuid=exam_id)
                if exam:
                    applicant_response = ApplicantResponseModel.objects.get(exam=exam, applicant=request.user.applicant)
                    applicant_response_serializer_data = ApplicantResponseModelGetSerializer(applicant_response, many=True).data
                    return Response(applicant_response_serializer_data, status=HTTP_200_OK)
                else:
                    return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Exam id is required'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization or applicant'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        exam_id = request.data.get('exam_id')
        if request.user.is_applicant:
            if exam_id:
                exam = ExamModel.objects.get(uuid=exam_id)
                if exam:
                    applicant_response_serializer = ApplicantResponseModelPostSerializer(data={
                        'exam': exam_id,
                        'applicant': request.user.applicant.uuid,
                        'question': request.data.get('question'),
                        'option': request.data.get('option'),
                    })
                    if applicant_response_serializer.is_valid():
                        applicant_response = applicant_response_serializer.create(applicant_response_serializer.validated_data)
                        applicant_response_serializer_data = ApplicantResponseModelGetSerializer(applicant_response).data
                        return Response(applicant_response_serializer_data, status=HTTP_201_CREATED)
                    else:
                        return Response(applicant_response_serializer.errors, status=HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Exam id is required'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not applicant'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request):
        applicant_response_id = request.GET.get('applicant_response_id')
        applicant_response = ApplicantResponseModel.objects.get(uuid=applicant_response_id)
        if applicant_response:
            exam = applicant_response.exam
            if request.user.is_applicant:
                submission_time = request.data.get('submission_time')
                time_taken = submission_time - applicant_response.start_time
                is_late = time_taken > exam.duration

                applicant_response_serializer = ApplicantResponseModelPostSerializer(applicant_response, data={
                    'exam': applicant_response.exam.uuid,
                    'applicant': applicant_response.applicant.uuid,
                    'submission_time': submission_time,
                    'is_submitted': True,
                    'is_late': is_late,
                })
                if applicant_response_serializer.is_valid():
                    applicant_response = applicant_response_serializer.update(applicant_response, applicant_response_serializer.validated_data, is_applicant=True)
                    applicant_response_serializer_data = ApplicantResponseModelGetSerializer(applicant_response).data
                    return Response(applicant_response_serializer_data, status=HTTP_201_CREATED)
                else:
                    return Response(applicant_response_serializer.errors, status=HTTP_400_BAD_REQUEST)
            elif request.user.organization:
                total_marks = request.data.get('total_marks')
                is_passed = False
                if total_marks >= exam.pass_marks:
                    is_passed = True

                applicant_response_serializer = ApplicantResponseModelPostSerializer(applicant_response, data={
                    'exam': applicant_response.exam.uuid,
                    'applicant': applicant_response.applicant.uuid,
                    'total_marks': total_marks,
                    'is_passed': is_passed,
                })
                if applicant_response_serializer.is_valid():
                    applicant_response = applicant_response_serializer.update(applicant_response, applicant_response_serializer.validated_data, is_applicant=False)
                    applicant_response_serializer_data = ApplicantResponseModelGetSerializer(applicant_response).data
                    return Response(applicant_response_serializer_data, status=HTTP_201_CREATED)
                else:
                    return Response(applicant_response_serializer.errors, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Applicant response does not exist'}, status=HTTP_400_BAD_REQUEST)


class QuestionResponseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        applicant_response_id = request.GET.get('applicant_response_id')
        if applicant_response_id:
            applicant_response = ApplicantResponseModel.objects.get(uuid=applicant_response_id)
            if applicant_response:
                question_responses = QuestionResponseModel.objects.filter(applicant_response=applicant_response)
                question_response_serializer_data = QuestionResponseModelGetSerializer(question_responses, many=True).data
                return Response(question_response_serializer_data, status=HTTP_200_OK)
            else:
                return Response({'error': 'Applicant response does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Applicant response id is required'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        applicant_response_id = request.data.get('applicant_response_id')
        question_id = request.data.get('question_id')
        options = request.data.get('options')
        if applicant_response_id and question_id:
            applicant_response = ApplicantResponseModel.objects.get(uuid=applicant_response_id)
            question = QuestionModel.objects.get(uuid=question_id)
            if applicant_response and question:
                is_correct = False
                if question.type == 'MCQ' or question.type == 'MCQ-M' or question.type == 'TF':
                    options = options[1:-1].split(', ')
                    options_list = [OptionModel.objects.get(uuid=option_id) for option_id in options]
                    for option in options_list:
                        if option.is_correct:
                            is_correct = True
                        else:
                            is_correct = False
                            break
                elif question.type == 'WA':
                    is_correct = False

                question_response_serializer = QuestionResponseModelPostSerializer(data={
                    'applicant_response': applicant_response_id,
                    'question': request.data.get('question'),
                    'option': request.data.get('option'),
                })
                if question_response_serializer.is_valid():
                    question_response = question_response_serializer.create(question_response_serializer.validated_data, is_correct)
                    question_response_serializer_data = QuestionResponseModelGetSerializer(question_response).data
                    return Response(question_response_serializer_data, status=HTTP_201_CREATED)
                else:
                    return Response(question_response_serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Applicant response does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Applicant response id is required'}, status=HTTP_400_BAD_REQUEST)