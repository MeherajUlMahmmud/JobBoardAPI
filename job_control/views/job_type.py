from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination
from job_control.models import JobTypeModel
from job_control.serializers.job_type import JobTypeModelSerializer


class JobTypeModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = JobTypeModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return JobTypeModelSerializer.Write
        return JobTypeModelSerializer.List
