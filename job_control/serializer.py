from rest_framework import serializers

from job_control.models import JobModel, JobTypeModel, JobApplicationModel
from user_control.models import OrganizationModel
from user_control.serializers import OrganizationModelSerializer, ApplicantModelSerializer


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTypeModel
        fields = ('uuid', 'name',)


class JobModelGetSerializer(serializers.ModelSerializer):
    job_types = JobTypeSerializer(many=True, read_only=True)

    class Meta:
        model = JobModel
        fields = ('uuid', 'organization', 'title', 'description', 'department', 'location', 'job_types')
        depth = 1

    def get_job_types(self, obj):
        return obj.job_types.all().values_list('name', flat=True)


class JobModelPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobModel
        fields = ('uuid', 'organization', 'title', 'description', 'department', 'location')

    def create(self, validated_data, job_types):
        job = JobModel.objects.create(
            organization=validated_data['organization'],
            title=validated_data['title'],
            description=validated_data['description'],
            department=validated_data['department'],
            location=validated_data['location'],
        )
        for job_type in job_types:
            job.job_types.add(job_type)

        return job

    def update(self, instance, validated_data, job_types):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.department = validated_data.get('department', instance.department)
        instance.location = validated_data.get('location', instance.location)
        instance.job_types.clear()
        for job_type in job_types:
            instance.job_types.add(job_type)
        instance.save()
        return instance


class JobApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicationModel
        fields = ('uuid', 'job', 'applicant', 'cover_letter')

    def save(self, **kwargs):
        job = self.validated_data['job']
        applicant = self.validated_data['applicant']
        cover_letter = self.validated_data['cover_letter']

        job_application = JobApplicationModel.objects.create(
            job=job,
            applicant=applicant,
            cover_letter=cover_letter,
        )

        return job_application


class JobApplicationDetailSerializer(serializers.ModelSerializer):
    job = serializers.SerializerMethodField()
    applicant = serializers.SerializerMethodField()

    class Meta:
        model = JobApplicationModel
        fields = ('uuid', 'job', 'applicant', 'cover_letter', 'status')

    def get_job(self, obj):
        return JobModelGetSerializer(obj.job).data

    def get_applicant(self, obj):
        return ApplicantModelSerializer(obj.applicant).data
