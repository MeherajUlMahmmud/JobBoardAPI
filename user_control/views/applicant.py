from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN

from common.custom_permissions import AdminOrStaffUserPermission
from common.custom_view import (
    CustomUpdateAPIView, CustomRetrieveAPIView, CustomListAPIView,
)
from common.utils import save_picture_to_folder
from user_control.custom_filters import ApplicantModelFilter
from user_control.models import ApplicantModel
from user_control.serializers.applicant import ApplicantModelSerializer


class GetApplicantListAPIView(CustomListAPIView):
    queryset = ApplicantModel.objects.filter(is_active=True, is_deleted=False)
    permission_classes = [AdminOrStaffUserPermission]
    serializer_class = ApplicantModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = ApplicantModelFilter
    search_fields = ['user__username', 'user__email', 'first_name', 'last_name']


class GetApplicantDetailsAPIView(CustomRetrieveAPIView):
    queryset = ApplicantModel.objects.filter(is_active=True, is_deleted=False)
    permission_classes = [AllowAny]
    serializer_class = ApplicantModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = ApplicantModelSerializer.List(instance)
        return Response(serializer.data, status=HTTP_200_OK)


class UpdateApplicantDetailsAPIView(CustomUpdateAPIView):
    queryset = ApplicantModel.objects.filter(is_active=True, is_deleted=False)
    serializer_class = ApplicantModelSerializer.Write

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({
                'detail': 'You do not have permission to perform this action.'
            }, status=HTTP_403_FORBIDDEN)

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


class UpdateApplicantProfilePictureAPIView(CustomUpdateAPIView):
    queryset = ApplicantModel.objects.filter(is_active=True, is_deleted=False)
    serializer_class = ApplicantModelSerializer.UpdateProfilePicture

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if instance.user != requested_user:
            return Response({
                'detail': 'You do not have permission to perform this action.'
            }, status=HTTP_403_FORBIDDEN)

        data = request.data
        serializer = self.serializer_class(instance, data=data)
        if serializer.is_valid():
            profile_picture = request.FILES.get('profile_picture')
            picture_path = save_picture_to_folder(profile_picture, 'profile_pictures')
            serializer.validated_data['profile_picture'] = picture_path
            serializer.save(
                updated_by=request.user,
            )
            return Response({
                'profile_picture': picture_path,
            }, status=HTTP_200_OK)
