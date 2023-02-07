from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED


from exam_control.models import ExamModel, QuestionModel, ApplicantResponseModel, OptionModel
from exam_control.serializers import ExamModelGetSerializer, ExamModelPostSerializer, QuestionModelGetSerializer, QuestionModelPostSerializer, OptionModelGetSerializer, OptionModelPostSerializer, \
    ApplicantResponseDetailSerializer
from job_control.models import JobModel, JobApplicationModel


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
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)

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
                    exam_serializer.create(exam_serializer.validated_data)
                    return Response(exam_serializer.data, status=HTTP_201_CREATED)
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
                    exam_serializer.update(exam, exam_serializer.validated_data)
                    return Response(exam_serializer.data, status=HTTP_201_CREATED)
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
                question_serializer = QuestionModelGetSerializer(question)
                return Response(question_serializer.data, status=HTTP_200_OK)
            else:
                return Response({'error': 'Question does not exist'}, status=HTTP_400_BAD_REQUEST)
        elif exam_id:
            exam = ExamModel.objects.get(uuid=exam_id)
            if exam:
                questions = QuestionModel.objects.filter(exam=exam)
                question_serializer = QuestionModelGetSerializer(questions, many=True)
                return Response(question_serializer.data, status=HTTP_200_OK)
            else:
                return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
        elif question_id:
            question = QuestionModel.objects.get(uuid=question_id)
            if question:
                question_serializer = QuestionModelGetSerializer(question)
                return Response(question_serializer.data, status=HTTP_200_OK)
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
                    question_serializer.create(question_serializer.validated_data)
                    return Response(question_serializer.data, status=HTTP_201_CREATED)
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
                    question_serializer.update(question, question_serializer.validated_data)
                    return Response(question_serializer.data, status=HTTP_201_CREATED)
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
            serializer = OptionModelGetSerializer(options, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
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
                    option_serializer.create(option_serializer.validated_data)
                    return Response(option_serializer.data, status=HTTP_201_CREATED)
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
                    option_serializer.update(option, option_serializer.validated_data)
                    return Response(option_serializer.data, status=HTTP_201_CREATED)
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
        exam = ExamModel.objects.get(uuid=exam_id, is_active=True, is_deleted=False)
        applicant = request.user.applicant
        responses = ApplicantResponseModel.objects.filter(exam=exam, applicant=applicant)
        serializer = ApplicantResponseDetailSerializer(responses, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        pass