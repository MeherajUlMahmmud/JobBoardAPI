from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from resume_control.custom_filters import ExperienceModelFilter
from resume_control.models import ExperienceModel
from resume_control.serializers.experience import ExperienceModelSerializer


class ExperienceModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = ExperienceModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    filterset_class = ExperienceModelFilter


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ExperienceModelSerializer.Write
        return ExperienceModelSerializer.List

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super(ExperienceModelViewSet, self).create(request, *args, **kwargs)
