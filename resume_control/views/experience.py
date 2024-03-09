from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView, CustomDestroyAPIView,
)
from resume_control.custom_filters import ExperienceModelFilter
from resume_control.models import ExperienceModel, ResumeModel
from resume_control.serializers.experience import ExperienceModelSerializer


class GetExperienceListAPIView(CustomListAPIView):
    serializer_class = ExperienceModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = ExperienceModelFilter
    search_fields = [
        'company_name',
        'position',
    ]

    def get_queryset(self):
        resume = get_object_or_404(ResumeModel, id=self.kwargs['resume_id'])
        if not self.request.user.check_object_permissions(self.request, resume):
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )
        return ExperienceModel.objects.filter(resume_id=resume.id)


class GetExperienceDetailsAPIView(CustomRetrieveAPIView):
    queryset = ExperienceModel.objects.all()
    serializer_class = ExperienceModelSerializer.List

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


class CreateExperienceAPIView(CustomCreateAPIView):
    queryset = ExperienceModel.objects.all()
    serializer_class = ExperienceModelSerializer.Write

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(
            data=data, context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(
            created_by=request.user,
        )
        return Response(
            serializer.data,
            status=HTTP_201_CREATED
        )


class UpdateExperienceDetailsAPIView(CustomUpdateAPIView):
    queryset = ExperienceModel.objects.all()
    serializer_class = ExperienceModelSerializer.Write

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.check_object_permissions(request, instance):
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


class DestroyExperienceAPIView(CustomDestroyAPIView):
    queryset = ExperienceModel.objects.all()
    serializer_class = ExperienceModelSerializer.List

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.check_object_permissions(request, instance):
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )
        instance.delete()
        return Response(
            status=HTTP_204_NO_CONTENT
        )
