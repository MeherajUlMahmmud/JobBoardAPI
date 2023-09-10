from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from .applicant import ApplicantModelSerializer
from .organization import OrganizationModelSerializer
from ..models import UserModel


class UserModelSerializerMeta(ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'id',
            'email',
            'is_applicant',
            'is_organization',
            'is_verified',
            'is_staff',
            'is_superuser',
        ]


class UserModelSerializer:
    class List(UserModelSerializerMeta):
        applicant = ApplicantModelSerializer.List()
        organization = OrganizationModelSerializer.List()

        class Meta(UserModelSerializerMeta.Meta):
            fields = UserModelSerializerMeta.Meta.fields + [
                'applicant',
                'organization',
            ]

    class Lite(UserModelSerializerMeta):
        class Meta(UserModelSerializerMeta.Meta):
            fields = [
                'email',
                'is_verified',
                'is_staff',
                'is_superuser',
            ]

    class Write(UserModelSerializerMeta):
        first_name = CharField(write_only=True, required=False, )
        last_name = CharField(write_only=True, required=False, )
        name = CharField(write_only=True, required=False, )
        password = CharField(write_only=True, required=True)

        class Meta(UserModelSerializerMeta.Meta):
            fields = UserModelSerializerMeta.Meta.fields + [
                'first_name',
                'last_name',
                'name',
                'password',
            ]
