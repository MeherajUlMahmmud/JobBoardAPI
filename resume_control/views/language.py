from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView,
)
from resume_control.custom_filters import LanguageModelFilter
from resume_control.models import LanguageModel
from resume_control.serializers.language import LanguageModelSerializer


class LanguageModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options',
                         'post', 'put', 'patch', 'delete']
    queryset = LanguageModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = LanguageModelFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LanguageModelSerializer.Write
        return LanguageModelSerializer.List


class GetLanguageListAPIView(CustomListAPIView):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageModelSerializer.List
    lookup_field = 'resume_id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.user.id:
            languages = LanguageModel.objects.filter(resume_id=instance.id)
            return Response(
                self.serializer_class(languages, many=True).data,
                status=HTTP_200_OK
            )
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )


class GetLanguageDetailsAPIView(CustomRetrieveAPIView):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.resume.user.id:
            return Response(
                self.serializer_class(instance).data,
                status=HTTP_200_OK
            )
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )


class CreateLanguageAPIView(CustomCreateAPIView):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageModelSerializer.Write
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


class UpdateLanguageDetailsAPIView(CustomUpdateAPIView):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageModelSerializer.Write

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.resume_id:
            return self.partial_update(request, *args, **kwargs)
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )
