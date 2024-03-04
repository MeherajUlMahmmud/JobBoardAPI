from rest_framework.serializers import ModelSerializer

from user_control.models import ApplicantModel
from user_control.serializers.user import UserModelSerializer


class ApplicantModelSerializerMeta(ModelSerializer):
    class Meta:
        model = ApplicantModel
        ref_name = 'ApplicantModelSerializer'
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
        ]


class ApplicantModelSerializer:
    class List(ApplicantModelSerializerMeta):
        class Meta(ApplicantModelSerializerMeta.Meta):
            fields = ApplicantModelSerializerMeta.Meta.fields + [
                'profile_picture',
                'user',
            ]

    class Details(ApplicantModelSerializerMeta):
        user = UserModelSerializer.Lite()

        class Meta(ApplicantModelSerializerMeta.Meta):
            fields = ApplicantModelSerializerMeta.Meta.fields + [
                'profile_picture',
                'user',
            ]

    class Lite(ApplicantModelSerializerMeta):
        class Meta(ApplicantModelSerializerMeta.Meta):
            fields = ApplicantModelSerializerMeta.Meta.fields + [
                'profile_picture',
            ]

    class Write(ApplicantModelSerializerMeta):
        class Meta(ApplicantModelSerializerMeta.Meta):
            fields = ApplicantModelSerializerMeta.Meta.fields
