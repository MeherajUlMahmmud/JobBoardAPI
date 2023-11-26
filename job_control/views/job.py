from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from common.custom_pagination import CustomPageNumberPagination
from common.custom_permissions import AdminOrStaffUserPermission
from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView,
)
from job_control.models import JobModel
from job_control.serializers.job import JobModelSerializer
from user_control.models import OrganizationModel


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
    permission_classes = [AdminOrStaffUserPermission]
    serializer_class = JobModelSerializer.List

    def get(self, request, *args, **kwargs):
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser:
            return self.list(request, *args, **kwargs)
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )


class GetJobListByOrganizationAPIView(CustomListAPIView):
    queryset = JobModel.objects.all()
    serializer_class = JobModelSerializer.ListForOthers
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']

    def get_queryset(self):
        organization = get_object_or_404(OrganizationModel, id=self.kwargs['org_id'])
        queryset = JobModel.objects.filter(organization_id=organization.id).order_by('-created_at')
        return queryset


class GetJobDetailsAPIView(CustomRetrieveAPIView):
    queryset = JobModel.objects.all()
    serializer_class = JobModelSerializer.Details

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


# class CreateJobAPIView(CustomCreateAPIView):
#     queryset = JobModel.objects.all()
#     serializer_class = JobModelSerializer.Write
#
#
# class UpdateJobAPIView(CustomUpdateAPIView):
#     queryset = JobModel.objects.all()
#     serializer_class = JobModelSerializer.Write
