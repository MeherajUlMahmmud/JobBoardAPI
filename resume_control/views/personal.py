from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from resume_control.custom_filters import PersonalModelFilter
from resume_control.serializers.personal import PersonalModelSerializer


class PersonalModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    serializer_class = PersonalModelSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PersonalModelFilter
    
    def get_queryset(self):
        resume = self.request.query_params.get('resume', None)
        if resume is not None:
            return self.queryset.filter(resume=resume)
        return self.queryset
