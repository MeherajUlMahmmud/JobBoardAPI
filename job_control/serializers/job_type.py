from rest_framework.serializers import ModelSerializer

from job_control.models import JobTypeModel


class JobTypeModelSerializerMeta(ModelSerializer):
    class Meta:
        model = JobTypeModel
        fields = [
            'name',
        ]


class JobTypeModelSerializer(JobTypeModelSerializerMeta):
    class List(JobTypeModelSerializerMeta):
        class Meta(JobTypeModelSerializerMeta.Meta):
            fields = JobTypeModelSerializerMeta.Meta.fields + [
                'uuid',
                'created_at',
                'updated_at',
            ]

    class Detail(JobTypeModelSerializerMeta):
        class Meta(JobTypeModelSerializerMeta.Meta):
            fields = JobTypeModelSerializerMeta.Meta.fields + [
                'uuid',
                'created_at',
                'updated_at',
            ]

    class Write(JobTypeModelSerializerMeta):
        class Meta(JobTypeModelSerializerMeta.Meta):
            fields = JobTypeModelSerializerMeta.Meta.fields
