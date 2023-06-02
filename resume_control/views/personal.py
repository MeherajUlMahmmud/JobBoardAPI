from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from resume_control.custom_filters import PersonalModelFilter
from resume_control.models import PersonalModel
from resume_control.serializers.personal import PersonalModelSerializer


class PersonalModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = PersonalModel.objects.all().order_by('-created_at')
    serializer_class = PersonalModelSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = PersonalModelFilter
