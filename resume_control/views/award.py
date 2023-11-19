from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView,
)
from resume_control.custom_filters import AwardModelFilter
from resume_control.models import AwardModel
from resume_control.serializers.award import AwardModelSerializer


class AwardModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options',
                         'post', 'put', 'patch', 'delete']
    queryset = AwardModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = AwardModelFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AwardModelSerializer.Write
        return AwardModelSerializer.List


class GetAwardListAPIView(CustomListAPIView):
    queryset = AwardModel.objects.all()
    serializer_class = AwardModelSerializer.List
    lookup_field = 'resume_id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.user.id:
            awards = AwardModel.objects.filter(resume_id=instance.id)
            return Response(
                self.serializer_class(awards, many=True).data,
                status=HTTP_200_OK
            )
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )


class GetAwardDetailsAPIView(CustomRetrieveAPIView):
    queryset = AwardModel.objects.all()
    serializer_class = AwardModelSerializer.List

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


class CreateAwardAPIView(CustomCreateAPIView):
    queryset = AwardModel.objects.all()
    serializer_class = AwardModelSerializer.Write
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


class UpdateAwardDetailsAPIView(CustomUpdateAPIView):
    queryset = AwardModel.objects.all()
    serializer_class = AwardModelSerializer.Write

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
