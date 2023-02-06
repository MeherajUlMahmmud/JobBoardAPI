from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView

from exam_control.models import ExamModel, QuestionModel, ApplicantResponseModel
from exam_control.serializers import ExamDetailSerializer, QuestionDetailSerializer, ApplicantResponseDetailSerializer, \
    ExamCreateSerializer, ExamSerializer, QuestionCreateSerializer, OptionCreateSerializer, OptionModelSerializer
from job_control.models import JobModel, JobApplicationModel


class ExamAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        job_id = request.GET.get('job_id')
        if request.user.is_organization:
            job = JobModel.objects.get(uuid=job_id, organization=request.user.organization)
            exams = ExamModel.objects.filter(job=job, is_active=True, organization=request.user.organization)
            serializer = ExamSerializer(exams, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        elif request.user.is_applicant:
            job = JobModel.objects.get(uuid=job_id, is_active=True, is_deleted=False)
            is_applied = JobApplicationModel.objects.filter(job=job, applicant=request.user.applicant).exists()
            if is_applied:
                exams = ExamModel.objects.filter(job=job, is_active=True)
                serializer = ExamSerializer(exams, many=True)
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                return Response({'error': 'You have not applied to this job'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is neither applicant nor organization'}, status=HTTP_400_BAD_REQUEST)

    def post(self, request):
        job_id = request.data.get('job_id')
        print(request.data)
        if request.user.is_organization:
            job = JobModel.objects.get(uuid=job_id, organization=request.user.organization)
            if job:
                exam_serializer = ExamCreateSerializer(data={
                    'job': job_id,
                    'organization': request.user.organization.uuid,
                    'name': request.data.get('name'),
                    'description': request.data.get('description'),
                    'allocated_time': request.data.get('allocated_time'),
                    'pass_marks': request.data.get('pass_marks'),
                })
                if exam_serializer.is_valid():
                    exam_serializer.save()
                    return Response(exam_serializer.data, status=HTTP_201_CREATED)
                else:
                    return Response(exam_serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Job does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)


class QuestionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        exam_id = request.GET.get('exam_id')
        question_id = request.GET.get('question_id')
        if exam_id:
            exam = ExamModel.objects.get(uuid=exam_id)
            questions = QuestionModel.objects.filter(exam=exam)
            serializer = QuestionDetailSerializer(questions, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        elif question_id:
            question = QuestionModel.objects.get(uuid=question_id)
            serializer = QuestionDetailSerializer(question)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response({'error': 'No exam or question id provided'}, status=HTTP_400_BAD_REQUEST)

    def post(self, request):
        exam_id = request.data.get('exam_id')
        if request.user.is_organization:
            exam = ExamModel.objects.get(uuid=exam_id, is_active=True, is_deleted=False)
            if exam:
                question_serializer = QuestionCreateSerializer(data={
                    'exam': exam_id,
                    'question': request.data.get('question'),
                    'type': request.data.get('type'),
                    'marks': request.data.get('marks'),
                })
                if question_serializer.is_valid():
                    question_serializer.save()
                    return Response(question_serializer.data, status=HTTP_201_CREATED)
                else:
                    return Response(question_serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Exam does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)


class OptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        question_id = request.GET.get('question_id')
        if question_id:
            question = QuestionModel.objects.get(uuid=question_id)
            serializer = OptionModelSerializer(question.options, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response({'error': 'No question id provided'}, status=HTTP_400_BAD_REQUEST)

    def post(self, request):
        question_id = request.data.get('question_id')
        if request.user.is_organization:
            question = QuestionModel.objects.get(uuid=question_id, is_active=True, is_deleted=False)
            if question:
                option_serializer = OptionCreateSerializer(data={
                    'question': question_id,
                    'option': request.data.get('option'),
                    'is_correct': request.data.get('is_correct'),
                })
                if option_serializer.is_valid():
                    option_serializer.save()
                    return Response(option_serializer.data, status=HTTP_201_CREATED)
                else:
                    return Response(option_serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Question does not exist'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)


class ApplicantResponseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        exam_id = request.GET.get('exam_id')
        exam = ExamModel.objects.get(uuid=exam_id, is_active=True, is_deleted=False)
        applicant = request.user.applicant
        responses = ApplicantResponseModel.objects.filter(exam=exam, applicant=applicant)
        serializer = ApplicantResponseDetailSerializer(responses, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        pass