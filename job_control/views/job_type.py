from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from common.custom_permissions import AdminOrStaffUserPermission
from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView,
)
from job_control.custom_filters import JobTypeModelFilter
from job_control.models import JobTypeModel
from job_control.serializers.job_type import JobTypeModelSerializer


class GetJobTypeListAPIView(CustomListAPIView):
    queryset = JobTypeModel.objects.all().order_by('-created_at')
    serializer_class = JobTypeModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = JobTypeModelFilter
    permission_classes = []


class GetJobTypeDetailsAPIView(CustomRetrieveAPIView):
    queryset = JobTypeModel.objects.all()
    serializer_class = JobTypeModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if not request.user.check_object_permissions(request, instance):
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )

        return Response(
            self.serializer_class(instance).data,
            status=HTTP_200_OK
        )


class CreateJobTypeAPIView(CustomCreateAPIView):
    queryset = JobTypeModel.objects.all()
    serializer_class = JobTypeModelSerializer.Write
    permission_classes = [AdminOrStaffUserPermission]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateJobTypeDetailsAPIView(CustomUpdateAPIView):
    queryset = JobTypeModel.objects.all()
    serializer_class = JobTypeModelSerializer.Write
    permission_classes = [AdminOrStaffUserPermission]

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
