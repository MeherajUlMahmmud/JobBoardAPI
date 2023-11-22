from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from common.custom_permissions import AdminOrStaffUserPermission
from common.custom_view import (
    CustomCreateAPIView, CustomUpdateAPIView, CustomRetrieveAPIView, CustomListAPIView,
)
from user_control.custom_filters import UserModelFilter
from user_control.models import UserModel, ApplicantModel, OrganizationModel
from user_control.serializers.applicant import ApplicantModelSerializer
from user_control.serializers.organization import OrganizationModelSerializer
from user_control.serializers.user import UserModelSerializer


class GetUserListAPIView(CustomListAPIView):
    queryset = UserModel.objects.filter(is_active=True, is_deleted=False)
    serializer_class = UserModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = UserModelFilter
    search_fields = ['username', 'email', 'first_name', 'last_name']

    def get_permissions(self):
        return [AdminOrStaffUserPermission()]


class GetUserDetailsAPIView(CustomRetrieveAPIView):
    queryset = UserModel.objects.filter(is_active=True, is_deleted=False)
    serializer_class = UserModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.id:
            serializer = UserModelSerializer.List(instance)
            if instance.is_applicant:
                applicant_details = ApplicantModel.objects.get(user=instance)
                serialized_applicant_details = ApplicantModelSerializer.List(applicant_details).data
                return Response({
                    'user_data': serializer.data,
                    'applicant_data': serialized_applicant_details if instance.is_applicant else None,
                })
            elif instance.is_organization:
                organization_details = OrganizationModel.objects.get(user=instance)
                serialized_organization_details = OrganizationModelSerializer.List(organization_details).data
                return Response({
                    'user_data': serializer.data,
                    'organization_data': serialized_organization_details if instance.is_organization else None,
                })
            return Response({
                'user_details': serializer.data,
            })
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )


class CreateUserAPIView(CustomCreateAPIView):
    permission_classes = (AdminOrStaffUserPermission,)
    serializer_class = UserModelSerializer.Write
    queryset = UserModel.objects.filter(is_active=True, is_deleted=False)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        first_name = validated_data['first_name'] if 'first_name' in validated_data else None
        last_name = validated_data['last_name'] if 'last_name' in validated_data else None
        name = validated_data['name'] if 'name' in validated_data else None
        password = validated_data['password']
        is_applicant = validated_data['is_applicant'] if 'is_applicant' in validated_data else False
        is_organization = validated_data['is_organization'] if 'is_organization' in validated_data else False
        is_verified = validated_data['is_verified'] if 'is_verified' in validated_data else False
        is_staff = validated_data['is_staff'] if 'is_staff' in validated_data else False
        is_admin = validated_data['is_admin'] if 'is_admin' in validated_data else False

        if 'name' not in validated_data and 'first_name' not in validated_data and 'last_name' not in validated_data:
            return Response(
                {
                    'detail': 'For creating an organization, name is required. For creating an applicant, first_name and last_name are required.'
                },
                status=HTTP_403_FORBIDDEN
            )
        if is_applicant and is_organization:
            return Response({
                'detail': 'User cannot be both applicant and organization.'}, status=HTTP_403_FORBIDDEN
            )
        if not is_applicant and not is_organization:
            return Response(
                {'detail': 'User must be either applicant or organization.'}, status=HTTP_403_FORBIDDEN
            )

        user = UserModel.objects.create(
            email=validated_data['email'],
            is_applicant=is_applicant,
            is_organization=is_organization,
            is_verified=is_verified,
            is_staff=is_staff,
            is_admin=is_admin,
            is_superuser=is_admin,
        )
        user.set_password(password)
        user.save()

        if is_applicant:
            ApplicantModel.objects.create(user=user, first_name=first_name, last_name=last_name)
        elif is_organization:
            OrganizationModel.objects.create(user=user, name=name)

        return Response(status=HTTP_200_OK)


class UpdateUserDetailsAPIView(CustomUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserModelSerializer.Write
    queryset = UserModel.objects.filter(is_active=True, is_deleted=False)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.id:
            serializer = self.serializer_class(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )
