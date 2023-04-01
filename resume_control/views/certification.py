from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from resume_control.models import CertificationModel
from resume_control.serializers.certification import CertificationModelSerializer


class CertificationModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = CertificationModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CertificationModelSerializer.Write
        return CertificationModelSerializer.List
