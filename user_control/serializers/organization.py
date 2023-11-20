from rest_framework.serializers import ModelSerializer

from user_control.models import OrganizationModel


class OrganizationModelSerializerMeta(ModelSerializer):
    class Meta:
        model = OrganizationModel
        ref_name = 'OrganizationModelSerializer'
        fields = [
            'id',
            'name',
            'company_logo',
            'cover_picture',
            'phone_number',
            'website',
            'description',
        ]


class OrganizationModelSerializer:
    class List(OrganizationModelSerializerMeta):
        class Meta(OrganizationModelSerializerMeta.Meta):
            fields = OrganizationModelSerializerMeta.Meta.fields

    class Write(OrganizationModelSerializerMeta):
        class Meta(OrganizationModelSerializerMeta.Meta):
            fields = OrganizationModelSerializerMeta.Meta.fields
