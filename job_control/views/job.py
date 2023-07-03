from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination
from job_control.models import JobModel
from job_control.serializers.job import JobModelSerializer


class JobModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = JobModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']

    # filterset_class = ResumeModelFilter

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return JobModelSerializer.Write
        return JobModelSerializer.List
