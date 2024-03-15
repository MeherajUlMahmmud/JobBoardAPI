from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, response, status

from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView, CustomDestroyAPIView,
)
from resume_control.custom_filters import ReferenceModelFilter
from resume_control.models import ReferenceModel, ResumeModel
from resume_control.serializers.reference import ReferenceModelSerializer


class GetReferenceListAPIView(CustomListAPIView):
    serializer_class = ReferenceModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = ReferenceModelFilter

    def get_queryset(self):
        resume = ResumeModel.objects.get(id=self.kwargs['resume_id'])
        if not self.request.user.check_object_permissions(self.request, resume):
            return response.Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=status.HTTP_403_FORBIDDEN
            )
        return ReferenceModel.objects.filter(resume_id=resume.id)


class GetReferenceDetailsAPIView(CustomRetrieveAPIView):
    queryset = ReferenceModel.objects.all()
    serializer_class = ReferenceModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.check_object_permissions(request, instance):
            return response.Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = self.serializer_class(instance)
        return response.Response(serializer.data)


class CreateReferenceAPIView(CustomCreateAPIView):
    queryset = ReferenceModel.objects.all()
    serializer_class = ReferenceModelSerializer.Write

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


class UpdateReferenceDetailsAPIView(CustomUpdateAPIView):
    queryset = ReferenceModel.objects.all()
    serializer_class = ReferenceModelSerializer.Write

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


class DestroyReferenceAPIView(CustomDestroyAPIView):
    queryset = ReferenceModel.objects.all()
    serializer_class = ReferenceModelSerializer.List

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