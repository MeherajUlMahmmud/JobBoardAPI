from rest_framework.serializers import ModelSerializer

from job_control.models import JobModel
from user_control.serializers.organization import OrganizationModelSerializer


class JobModelSerializerMeta(ModelSerializer):
    class Meta:
        model = JobModel
        fields = [
            'title',
            'description',
        ]


class JobModelSerializer(JobModelSerializerMeta):
    class List(JobModelSerializerMeta):
        organization = OrganizationModelSerializer.List()

        class Meta(JobModelSerializerMeta.Meta):
            fields = JobModelSerializerMeta.Meta.fields + [
                'uuid',
                'organization',
                'department',
                'location',
                'job_types',
                'is_fixed_salary',
                'salary',
                'salary_currency',
                'salary_period',
                'salary_min',
                'salary_max',
                'created_at',
                'updated_at',
            ]

    class Detail(JobModelSerializerMeta):
        organization = OrganizationModelSerializer.List()

        class Meta(JobModelSerializerMeta.Meta):
            fields = JobModelSerializerMeta.Meta.fields + [
                'uuid',
                'organization',
                'department',
                'location',
                'job_types',
                'is_fixed_salary',
                'salary',
                'salary_currency',
                'salary_period',
                'salary_min',
                'salary_max',
                'created_at',
                'updated_at',
            ]

    class Write(JobModelSerializerMeta):
        class Meta(JobModelSerializerMeta.Meta):
            fields = JobModelSerializerMeta.Meta.fields + [
                'organization',
                'department',
                'location',
                'job_types',
                'is_fixed_salary',
                'salary',
                'salary_currency',
                'salary_period',
                'salary_min',
                'salary_max',
            ]
