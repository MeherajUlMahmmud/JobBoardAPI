from rest_framework import serializers

from resume_control.models import *


class EducationModelSerializerMeta(serializers.ModelSerializer):
    class Meta:
        model = EducationModel
        fields = (
        'uuid', 'resume', 'school_name', 'degree', 'department', 'grade', 'start_date', 'end_date',
        'description')


class EducationModelSerializer:
    class List(EducationModelSerializerMeta):
        class Meta(EducationModelSerializerMeta.Meta):
            fields = EducationModelSerializerMeta.Meta.fields

    class Write(EducationModelSerializerMeta):
        class Meta(EducationModelSerializerMeta.Meta):
            fields = EducationModelSerializerMeta.Meta.fields
