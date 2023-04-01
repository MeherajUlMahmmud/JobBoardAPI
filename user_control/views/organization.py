from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination
from user_control.models import OrganizationModel
from user_control.serializers.organization import OrganizationModelSerializer


class OrganizationModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'put', 'patch', 'delete']
    queryset = OrganizationModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrganizationModelSerializer.List
        return OrganizationModelSerializer.Write
