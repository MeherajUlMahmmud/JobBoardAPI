from rest_framework.serializers import ModelSerializer

from resume_control.models import PersonalModel


class PersonalModelSerializer(ModelSerializer):
    class Meta:
        model = PersonalModel
        fields = [
            'uuid',
            'resume',
            'first_name',
            'last_name',
            'about_me',
            'date_of_birth',
            'nationality',
            'city',
            'state',
            'country',
        ]
