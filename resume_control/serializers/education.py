from rest_framework.serializers import (
    ModelSerializer, CharField, ValidationError,
)

from resume_control.models import *


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
            'serial',
        ]


class EducationModelSerializer:
    class List(EducationModelSerializerMeta):
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

    class UpdateSerial(EducationModelSerializerMeta):
        new_serial = CharField(required=True, write_only=True)

        class Meta(EducationModelSerializerMeta.Meta):
            fields = [
                'new_serial',
            ]

        def validate(self, attrs):
            new_serial = attrs['new_serial']
            if not new_serial.isdigit():
                raise ValidationError('New serial must be a number.')
            if self.instance.serial == attrs['new_serial']:
                raise ValidationError('New serial can not be same as old serial.')
            return attrs
