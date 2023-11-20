from rest_framework.serializers import ModelSerializer

from job_control.models import JobTypeModel
from user_control.serializers.user import UserModelSerializer


class JobTypeModelSerializerMeta(ModelSerializer):
    class Meta:
        model = JobTypeModel
        fields = [
            'name',
        ]


class JobTypeModelSerializer(JobTypeModelSerializerMeta):
    class List(JobTypeModelSerializerMeta):
        created_by = UserModelSerializer.Lite(read_only=True)
        updated_by = UserModelSerializer.Lite(read_only=True)

        class Meta(JobTypeModelSerializerMeta.Meta):
            fields = JobTypeModelSerializerMeta.Meta.fields + [
                'id',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Write(JobTypeModelSerializerMeta):
        class Meta(JobTypeModelSerializerMeta.Meta):
            fields = JobTypeModelSerializerMeta.Meta.fields
