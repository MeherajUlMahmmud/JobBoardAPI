from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from resume_control.custom_filters import SkillModelFilter
from resume_control.models import SkillModel
from resume_control.serializers.skill import SkillModelSerializer


class SkillModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = SkillModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = SkillModelFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SkillModelSerializer.Write
        return SkillModelSerializer.List
