from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, response, status

from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView, CustomDestroyAPIView,
)
from resume_control.custom_filters import EducationModelFilter
from resume_control.models import EducationModel, ResumeModel
from resume_control.serializers.education import EducationModelSerializer


class GetEducationListAPIView(CustomListAPIView):
    serializer_class = EducationModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = EducationModelFilter
    search_fields = [
        'school_name',
        'degree',
        'department',
    ]

    def get_queryset(self):
        resume = get_object_or_404(ResumeModel, id=self.kwargs['resume_id'])
        if not self.request.user.check_object_permissions(self.request, resume):
            return response.Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=status.HTTP_403_FORBIDDEN
            )
        return EducationModel.objects.filter(resume_id=resume.id)


class GetEducationDetailsAPIView(CustomRetrieveAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.check_object_permissions(request, instance):
            return response.Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=status.HTTP_403_FORBIDDEN
            )
        return response.Response(
            self.serializer_class(instance).data,
            status=status.HTTP_200_OK
        )


class CreateEducationAPIView(CustomCreateAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationModelSerializer.Write

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(
            data=data, context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(
            created_by=request.user,
        )
        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class UpdateEducationDetailsAPIView(CustomUpdateAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationModelSerializer.Write

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        serializer = self.serializer_class(data=data, context={'request': request}, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            updated_by=request.user,
        )
        return response.Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class DestroyEducationAPIView(CustomDestroyAPIView):
    queryset = EducationModel.objects.all()
    serializer_class = EducationModelSerializer.List

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.check_object_permissions(request, instance):
            return response.Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=status.HTTP_403_FORBIDDEN
            )
        instance.delete()
        return response.Response(
            status=status.HTTP_204_NO_CONTENT
        )