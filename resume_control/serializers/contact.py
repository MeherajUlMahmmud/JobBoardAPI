from rest_framework.serializers import ModelSerializer

from resume_control.models import ContactModel
from user_control.serializers.user import UserModelSerializer


class ContactModelSerializerMeta(ModelSerializer):
    class Meta:
        model = ContactModel
        ref_name = 'ContactModelSerializer'
        fields = [
            'phone_number',
            'email',
            'address',
            'zip_code',
            'facebook',
            'linkedin',
            'github',
            'website',
        ]


class ContactModelSerializer:
    class List(ContactModelSerializerMeta):
        created_by = UserModelSerializer.Lite(read_only=True)
        updated_by = UserModelSerializer.Lite(read_only=True)

        class Meta(ContactModelSerializerMeta.Meta):
            fields = ContactModelSerializerMeta.Meta.fields + [
                'id',
                'resume',
                'created_by',
                'created_at',
                'updated_by',
                'updated_at',
            ]

    class Write(ContactModelSerializerMeta):
        class Meta(ContactModelSerializerMeta.Meta):
            fields = ContactModelSerializerMeta.Meta.fields
