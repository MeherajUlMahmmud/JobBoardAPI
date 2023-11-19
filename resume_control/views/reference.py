from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView,
)
from resume_control.custom_filters import ReferenceModelFilter
from resume_control.models import ReferenceModel
from resume_control.serializers.reference import ReferenceModelSerializer


class ReferenceModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options',
                         'post', 'put', 'patch', 'delete']
    queryset = ReferenceModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = ReferenceModelFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ReferenceModelSerializer.Write
        return ReferenceModelSerializer.List


class GetReferenceListAPIView(CustomListAPIView):
    queryset = ReferenceModel.objects.all()
    serializer_class = ReferenceModelSerializer.List
    lookup_field = 'resume_id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        requested_user = request.user
        if requested_user.is_staff or requested_user.is_superuser or requested_user.id == instance.user.id:
            references = ReferenceModel.objects.filter(resume_id=instance.id)
            return Response(
                self.serializer_class(references, many=True).data,
                status=HTTP_200_OK
            )
        else:
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )


class GetDetailsReferenceAPIView(CustomRetrieveAPIView):
    queryset = ReferenceModel.objects.all()
    serializer_class = ReferenceModelSerializer.List

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


class CreateReferenceAPIView(CustomCreateAPIView):
    queryset = ReferenceModel.objects.all()
    serializer_class = ReferenceModelSerializer.Write
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


class UpdateReferenceAPIView(CustomUpdateAPIView):
    queryset = ReferenceModel.objects.all()
    serializer_class = ReferenceModelSerializer.Write

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
