from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from common.custom_permissions import AdminOrStaffUserPermission
from common.custom_view import (
    CustomUpdateAPIView, CustomRetrieveAPIView, CustomListAPIView,
)

from user_control.custom_filters import OrganizationModelFilter
from user_control.models import OrganizationModel
from user_control.serializers.organization import OrganizationModelSerializer


class GetOrganizationListAPIView(CustomListAPIView):
    queryset = OrganizationModel.objects.filter(is_active=True, is_deleted=False)
    permission_classes = [AdminOrStaffUserPermission]
    serializer_class = OrganizationModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = OrganizationModelFilter
    search_fields = ['user__username', 'user__email', 'name', ]


class GetOrganizationDetailsAPIView(CustomRetrieveAPIView):
    queryset = OrganizationModel.objects.filter(is_active=True, is_deleted=False)
    permission_classes = [AllowAny]
    serializer_class = OrganizationModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = OrganizationModelSerializer.List(instance)
        return Response(serializer.data, status=HTTP_200_OK)


class UpdateOrganizationDetailsAPIView(CustomUpdateAPIView):
    queryset = OrganizationModel.objects.filter(is_active=True, is_deleted=False)
    serializer_class = OrganizationModelSerializer.Write

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if not request.user.check_object_permissions(request, instance) or not requested_user.id == instance.user.id:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )

        data = request.data
        serializer = self.serializer_class(
            instance, data=data, context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(
            updated_by=request.user,
        )
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
