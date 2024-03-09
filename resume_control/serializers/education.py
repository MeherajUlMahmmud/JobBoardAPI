from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from resume_control.models import *
from user_control.serializers.user import UserModelSerializer


class EducationModelSerializerMeta(ModelSerializer):
    class Meta:
        model = EducationModel
        ref_name = 'EducationModelSerializer'
        fields = [
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
        ]


class EducationModelSerializer:
    class List(EducationModelSerializerMeta):
        # created_by = UserModelSerializer.Lite(read_only=True)
        # updated_by = UserModelSerializer.Lite(read_only=True)

        class Meta(EducationModelSerializerMeta.Meta):
            fields = EducationModelSerializerMeta.Meta.fields + [
                'id',
                'is_active',
                'is_deleted',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Write(EducationModelSerializerMeta):

        class Meta(EducationModelSerializerMeta.Meta):
            fields = EducationModelSerializerMeta.Meta.fields

        def validate(self, attrs):
            if attrs['resume'].user.id != self.context['request'].user.id:
                raise ValidationError('You are not allowed to create award for this resume.')
            return attrs
