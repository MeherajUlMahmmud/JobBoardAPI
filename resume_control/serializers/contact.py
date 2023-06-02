from rest_framework.serializers import ModelSerializer

from resume_control.models import ContactModel


class ContactModelSerializer(ModelSerializer):
    class Meta:
        model = ContactModel
        fields = [
            'uuid',
            'resume',
            'phone_number',
            'email',
            'address',
            'zip_code',
            'facebook',
            'linkedin',
            'github',
            'website',
        ]
