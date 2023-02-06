from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from job_control.models import JobTypeJobModel, JobTypeModel, JobModel, JobApplicationModel
from job_control.serializer import JobTypeSerializer, JobCreateSerializer, JobDetailSerializer, JobTypeJobSerializer, \
    JobApplicationCreateSerializer, JobApplicationDetailSerializer
from user_control.models import UserModel, ApplicantModel


class JobTypeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        job_types = JobTypeModel.objects.all()
        serializer = JobTypeSerializer(job_types, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class JobAPIView(APIView):
    permission_classes = [IsAuthenticated]
    paginate_by = 10

    def get(self, request):
        page = request.GET.get('page')
        organization = request.GET.get('organization')
        # job_type = request.GET.get('job_type')

        if organization:
            jobs = JobModel.objects.filter(organization=organization)
        # elif job_type:
        # 	jobs = JobModel.objects.filter(job_type_jobs__job_type=job_type)
        else:
            jobs = JobModel.objects.all()
        job_serializer = JobDetailSerializer(jobs, many=True)
        for job in job_serializer.data:
            job_type_jobs = JobTypeJobModel.objects.filter(job=job['uuid'])
            job['job_types'] = JobTypeJobSerializer(job_type_jobs, many=True).data
        return Response(job_serializer.data, status=HTTP_200_OK)

    def post(self, request):
        organization = request.data.get('organization')
        title = request.data.get('title')
        description = request.data.get('description')
        department = request.data.get('department')
        location = request.data.get('location')
        types = request.data.get('types')

        if types is None or len(types) < 1:
            return Response({'error': 'Job must have at least one type'}, status=HTTP_400_BAD_REQUEST)
        types = types[1:-1].split(', ')

        types_list = [JobTypeModel.objects.get(uuid=type_id) for type_id in types]

        job_serializer = JobCreateSerializer(data={
            'organization': organization,
            'title': title,
            'description': description,
            'department': department,
            'location': location,
        })
        if job_serializer.is_valid():
            job = job_serializer.save()

            job_type_jobs = []
            for type in types_list:
                job_type_jobs.append(JobTypeJobModel.objects.create(job=job, job_type=type))

            return Response(job_serializer.data, status=HTTP_201_CREATED)
        return Response(job_serializer.errors, status=HTTP_400_BAD_REQUEST)

    def patch(self, request):
        uuid = request.data.get('uuid')
        title = request.data.get('title')
        description = request.data.get('description')
        department = request.data.get('department')
        location = request.data.get('location')
        types = request.data.get('types')

        if types is None or len(types) < 1:
            return Response({'error': 'Job must have at least one type'}, status=HTTP_400_BAD_REQUEST)
        types = types[1:-1].split(', ')

        types_list = [JobTypeModel.objects.get(uuid=type_id) for type_id in types]

        job = JobModel.objects.get(uuid=uuid)
        job.title = title
        job.description = description
        job.department = department
        job.location = location
        job.save()

        job_type_jobs = JobTypeJobModel.objects.filter(job=job)
        job_type_jobs.delete()

        for type in types_list:
            JobTypeJobModel.objects.create(job=job, job_type=type)

        job_serializer = JobDetailSerializer(job)
        return Response(job_serializer.data, status=HTTP_200_OK)


class JobApplicationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        page = request.GET.get('page')
        job = request.GET.get('job')
        applicant = request.GET.get('applicant')

        if job and applicant:
            job_applications = JobApplicationModel.objects.filter(job=job, applicant=applicant)
        elif job:
            job_applications = JobApplicationModel.objects.filter(job=job)
        elif applicant:
            job_applications = JobApplicationModel.objects.filter(applicant=applicant)
        else:
            job_applications = JobApplicationModel.objects.all()
        job_application_serializer = JobApplicationDetailSerializer(job_applications, many=True)
        for job_application in job_application_serializer.data:
            job_application['job']['job_types'] = JobTypeJobSerializer(
                JobTypeJobModel.objects.filter(job=job_application['job']['uuid']), many=True).data

        return Response(job_application_serializer.data, status=HTTP_200_OK)

    def post(self, request):
        job = request.data.get('job')
        applicant = request.data.get('applicant')
        cover_letter = request.data.get('cover_letter')

        if JobApplicationModel.objects.filter(job=job, applicant=applicant).exists():
            return Response({'error': 'Job application already exists'}, status=HTTP_400_BAD_REQUEST)

        job_application_serializer = JobApplicationCreateSerializer(data={
            'job': job,
            'applicant': applicant,
            'cover_letter': cover_letter,
        })
        if job_application_serializer.is_valid():
            job_application = job_application_serializer.save()
            # job_type_jobs = JobTypeJobModel.objects.filter(job=job)
            # job_application_serializer.data['job']['job_types'] = JobTypeJobSerializer(job_type_jobs, many=True).data
            return Response(job_application_serializer.data, status=HTTP_201_CREATED)
        return Response(job_application_serializer.errors, status=HTTP_400_BAD_REQUEST)
