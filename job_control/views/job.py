from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from common.custom_pagination import CustomPageNumberPagination
from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView,
)
from job_control.models import JobModel
from job_control.serializers.job import JobModelSerializer


class JobModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options',
                         'post', 'put', 'patch', 'delete']
    queryset = JobModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return JobModelSerializer.Write
        return JobModelSerializer.List


class GetJobListAPIView(CustomListAPIView):
    queryset = JobModel.objects.all()
    serializer_class = JobModelSerializer.List
    lookup_field = 'resume_id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.user.id:
            jobs = JobModel.objects.filter(resume_id=instance.id)
            return Response(
                self.serializer_class(jobs, many=True).data,
                status=HTTP_200_OK
            )
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )


class GetDetailsJobAPIView(CustomRetrieveAPIView):
    queryset = JobModel.objects.all()
    serializer_class = JobModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.resume.user.id:
            return Response(
                self.serializer_class(instance).data,
                status=HTTP_200_OK
            )
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )


class CreateJobAPIView(CustomCreateAPIView):
    queryset = JobModel.objects.all()
    serializer_class = JobModelSerializer.Write
    lookup_field = 'resume_id'

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.user.id:
            return self.create(request, *args, **kwargs)
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )


class UpdateJobAPIView(CustomUpdateAPIView):
    queryset = JobModel.objects.all()
    serializer_class = JobModelSerializer.Write

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.resume_id:
            return self.partial_update(request, *args, **kwargs)
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )
