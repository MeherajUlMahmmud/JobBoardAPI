from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, response, status

from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView, CustomDestroyAPIView,
)
from resume_control.custom_filters import SkillModelFilter
from resume_control.models import SkillModel, ResumeModel
from resume_control.serializers.skill import SkillModelSerializer


class GetSkillListAPIView(CustomListAPIView):
    serializer_class = SkillModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = SkillModelFilter

    def get_queryset(self):
        resume = get_object_or_404(ResumeModel, id=self.kwargs['resume_id'])
        if not self.request.user.check_object_permissions(self.request, resume):
            return response.Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=status.HTTP_403_FORBIDDEN
            )
        return SkillModel.objects.filter(resume_id=resume.id)


class GetSkillDetailsAPIView(CustomRetrieveAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if not request.user.check_object_permissions(request, instance):
            return response.Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = SkillModelSerializer.List(instance)
        return response.Response(serializer.data)


class CreateSkillAPIView(CustomCreateAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillModelSerializer.Write

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


class UpdateSkillDetailsAPIView(CustomUpdateAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillModelSerializer.Write

    def patch(self, request, *args, **kwargs):
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


class DestroySkillAPIView(CustomDestroyAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillModelSerializer.Write

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