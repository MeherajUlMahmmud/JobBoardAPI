from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from resume_control.custom_filters import ReferenceModelFilter
from resume_control.models import ReferenceModel
from resume_control.serializers.reference import ReferenceModelSerializer


class ReferenceModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = ReferenceModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = ReferenceModelFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReferenceModelSerializer.Write
        return ReferenceModelSerializer.List
