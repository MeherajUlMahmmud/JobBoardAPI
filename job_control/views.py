from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from exam_control.models import ExamModel
from exam_control.serializers import ExamModelGetSerializer
from job_control.models import JobTypeModel, JobModel, JobApplicationModel
from job_control.serializer import JobModelGetSerializer, JobModelPostSerializer, JobTypeSerializer, \
    JobApplicationGetSerializer, JobApplicationPostSerializer


class JobTypeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        type_id = request.GET.get('type_id')
        if type_id:
            job_type = JobTypeModel.objects.get(uuid=type_id)
            serializer = JobTypeSerializer(job_type)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            job_types = JobTypeModel.objects.all()
            serializer = JobTypeSerializer(job_types, many=True)
            return Response(serializer.data, status=HTTP_200_OK)


class JobAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    paginate_by = 10

    @staticmethod
    def get(request):
        page = request.GET.get('page')
        job_id = request.GET.get('job_id')
        organization = request.GET.get('organization')
        # job_type = request.GET.get('job_type')

        if job_id and organization:
            job = JobModel.objects.get(uuid=job_id, organization=organization)
            serializer = JobModelGetSerializer(job)
            return Response(serializer.data, status=HTTP_200_OK)
        elif job_id:
            job = JobModel.objects.get(uuid=job_id)
            serializer = JobModelGetSerializer(job)
            return Response(serializer.data, status=HTTP_200_OK)
        elif organization:
            jobs = JobModel.objects.filter(organization=organization)
        else:
            jobs = JobModel.objects.all()

        job_serializer_data = JobModelGetSerializer(jobs, many=True).data
        return Response(job_serializer_data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        if request.user.is_organization:
            organization = request.user.organization
            types = request.data.get('types')

            if types is None or len(types) < 1:
                return Response({'error': 'Job must have at least one type'}, status=HTTP_400_BAD_REQUEST)
            types = types[1:-1].split(', ')
            types_list = [JobTypeModel.objects.get(uuid=type_id) for type_id in types]
            job_serializer = JobModelPostSerializer(data={
                'organization': organization.uuid,
                'title': request.data.get('title'),
                'description': request.data.get('description'),
                'department': request.data.get('department'),
                'location': request.data.get('location'),
            })
            if job_serializer.is_valid():
                job = job_serializer.create(job_serializer.validated_data, types_list)
                job_serializer_data = JobModelGetSerializer(job).data
                return Response(job_serializer_data, status=HTTP_201_CREATED)
            return Response(job_serializer.errors, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request):
        job_id = request.GET.get('job_id')
        if request.user.is_organization:
            organization = request.user.organization
            job = JobModel.objects.get(uuid=job_id, organization=organization)
            if job:
                types = request.data.get('types')

                if types is None or len(types) < 1:
                    return Response({'error': 'Job must have at least one type'}, status=HTTP_400_BAD_REQUEST)
                types = types[1:-1].split(', ')
                types_list = [JobTypeModel.objects.get(uuid=type_id) for type_id in types]
                job_serializer = JobModelPostSerializer(job, data={
                    'organization': request.data.get('organization'),
                    'title': request.data.get('title'),
                    'description': request.data.get('description'),
                    'department': request.data.get('department'),
                    'location': request.data.get('location'),
                })
                if job_serializer.is_valid():
                    job = job_serializer.update(job, job_serializer.validated_data, types_list)
                    job_serializer_data = JobModelPostSerializer(job).data
                    return Response(job_serializer_data, status=HTTP_201_CREATED)
                return Response(job_serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Job not found'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User is not organization'}, status=HTTP_400_BAD_REQUEST)


class JobApplicationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        # page = request.GET.get('page')
        job_id = request.GET.get('job_id')
        applicant_id = request.GET.get('applicant_id')
        application_id = request.GET.get('application_id')

        if job_id and applicant_id:
            job_applications = JobApplicationModel.objects.filter(job=job_id, applicant=applicant_id)
        elif job_id:
            job_applications = JobApplicationModel.objects.filter(job=job_id)
        elif applicant_id:
            job_applications = JobApplicationModel.objects.filter(applicant=applicant_id)
        elif application_id:
            job_application = JobApplicationModel.objects.get(uuid=application_id)
            exams = ExamModel.objects.filter(job=job_application.job)

            job_application_serializer_data = JobApplicationGetSerializer(job_application).data
            del job_application_serializer_data['applicant']['user']

            exam_serializer = ExamModelGetSerializer(exams, many=True).data
            for exam in exam_serializer:
                del exam['organization']
                del exam['job']

            return Response({"application": job_application_serializer_data,
                             "exams": exam_serializer}, status=HTTP_200_OK)
        else:
            job_applications = JobApplicationModel.objects.all()
        job_application_serializer_data = JobApplicationGetSerializer(job_applications, many=True).data

        for job_application in job_application_serializer_data:
            del job_application['applicant']['user']

        return Response(job_application_serializer_data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        job_id = request.data.get('job_id')
        applicant_id = request.data.get('applicant_id')
        cover_letter = request.data.get('cover_letter')

        if job_id and applicant_id:
            job_application = JobApplicationModel.objects.get(job=job_id, applicant=applicant_id)
            if job_application:
                return Response({'error': 'Job application already exists'}, status=HTTP_400_BAD_REQUEST)
            job_application_serializer = JobApplicationPostSerializer(data={
                'job': job_id,
                'applicant': applicant_id,
                'cover_letter': cover_letter,
            })

            if job_application_serializer.is_valid():
                job_application = job_application_serializer.create(job_application_serializer.validated_data)
                job_application_serializer_data = JobApplicationGetSerializer(job_application).data
                return Response(job_application_serializer_data, status=HTTP_201_CREATED)
            return Response(job_application_serializer.errors, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Job or applicant not found'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request):
        application_id = request.GET.get('application_id')
        job_application = JobApplicationModel.objects.get(uuid=application_id)
        if job_application:
            job_application_serializer = JobApplicationPostSerializer(job_application, data={
                'job': request.data.get('job'),
                'applicant': request.data.get('applicant'),
                'cover_letter': request.data.get('cover_letter'),
            })
            if job_application_serializer.is_valid():
                job_application = job_application_serializer.update(job_application,
                                                                    job_application_serializer.validated_data)
                job_application_serializer_data = JobApplicationGetSerializer(job_application).data
                return Response(job_application_serializer_data, status=HTTP_201_CREATED)
            return Response(job_application_serializer.errors, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Job application not found'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        application_id = request.GET.get('application_id')
        job_application = JobApplicationModel.objects.get(uuid=application_id)
        if job_application:
            job_application.delete()
            return Response({'message': 'Job application deleted'}, status=HTTP_200_OK)
        else:
            return Response({'error': 'Job application not found'}, status=HTTP_400_BAD_REQUEST)
