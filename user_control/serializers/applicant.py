from rest_framework.serializers import ModelSerializer

from user_control.models import ApplicantModel


class ApplicantModelSerializerMeta(ModelSerializer):
    class Meta:
        model = ApplicantModel
        fields = [
            'id',
            'first_name',
            'last_name',
            'profile_picture',
            'phone_number',
            'resume',
        ]


class ApplicantModelSerializer:
    class List(ApplicantModelSerializerMeta):
        class Meta(ApplicantModelSerializerMeta.Meta):
            fields = ApplicantModelSerializerMeta.Meta.fields

    class Lite(ApplicantModelSerializerMeta):
        class Meta(ApplicantModelSerializerMeta.Meta):
            fields = ApplicantModelSerializerMeta.Meta.fields

    class Write(ApplicantModelSerializerMeta):
        class Meta(ApplicantModelSerializerMeta.Meta):
            fields = ApplicantModelSerializerMeta.Meta.fields
