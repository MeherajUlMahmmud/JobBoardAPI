from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView,
)
from resume_control.custom_filters import SkillModelFilter
from resume_control.models import SkillModel
from resume_control.serializers.skill import SkillModelSerializer


class SkillModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = SkillModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = SkillModelFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SkillModelSerializer.Write
        return SkillModelSerializer.List


class GetSkillListAPIView(CustomListAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = SkillModelFilter
    lookup_field = 'resume_id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.user.id:
            skills = SkillModel.objects.filter(resume_id=instance.id)

            return Response(
                self.serializer_class(skills, many=True).data,
                status=HTTP_200_OK
            )
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )


class GetSkillDetailsAPIView(CustomRetrieveAPIView):
    queryset = SkillModel.objects.all()
    serializer_class = SkillModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.resume.user.id:
            serializer = SkillModelSerializer.List(instance)
            return Response(serializer.data)
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )


class CreateSkillAPIView(CustomCreateAPIView):
    serializer_class = SkillModelSerializer.Write
    queryset = SkillModel.objects.all()
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


class UpdateSkillDetailsAPIView(CustomUpdateAPIView):
    serializer_class = SkillModelSerializer.Write
    queryset = SkillModel.objects.all()

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.resume.user.id:
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
