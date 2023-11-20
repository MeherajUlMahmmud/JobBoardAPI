from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView,
)
from resume_control.custom_filters import SkillModelFilter
from resume_control.models import SkillModel, ResumeModel
from resume_control.serializers.skill import SkillModelSerializer


class GetSkillListAPIView(CustomListAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = SkillModelFilter

    def get(self, request, *args, **kwargs):
        resume = ResumeModel.objects.get(id=kwargs['resume_id'])

        if not request.user.check_object_permissions(request, resume):
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )

        skills = SkillModel.objects.filter(resume_id=resume.id)
        return Response(
            self.serializer_class(skills, many=True).data,
            status=HTTP_200_OK
        )


class GetSkillDetailsAPIView(CustomRetrieveAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if not request.user.check_object_permissions(request, instance):
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )

        serializer = SkillModelSerializer.List(instance)
        return Response(serializer.data)


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
        return Response(
            serializer.data,
            status=HTTP_200_OK
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
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
