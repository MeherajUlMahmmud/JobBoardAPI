from rest_framework.serializers import ModelSerializer

from resume_control.models import *


class EducationModelSerializerMeta(ModelSerializer):
    class Meta:
        model = EducationModel
        ref_name = 'EducationModelSerializer'
        fields = (
            'id',
            'resume',
            'school_name',
            'degree',
            'department',
            'grade_scale',
            'grade',
            'start_date',
            'is_current',
            'end_date',
            'description',
        )


class EducationModelSerializer:
    class List(EducationModelSerializerMeta):
        class Meta(EducationModelSerializerMeta.Meta):
            fields = EducationModelSerializerMeta.Meta.fields

    class Write(EducationModelSerializerMeta):
        class Meta(EducationModelSerializerMeta.Meta):
            fields = EducationModelSerializerMeta.Meta.fields
