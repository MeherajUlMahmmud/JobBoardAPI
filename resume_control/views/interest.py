from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from common.custom_view import (
    CustomListAPIView, CustomRetrieveAPIView, CustomCreateAPIView, CustomUpdateAPIView,
)
from resume_control.custom_filters import InterestModelFilter
from resume_control.models import InterestModel, ResumeModel
from resume_control.serializers.interest import InterestModelSerializer


class GetInterestListAPIView(CustomListAPIView):
    serializer_class = InterestModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = InterestModelFilter

    def get_queryset(self):
        resume = get_object_or_404(ResumeModel, id=self.kwargs['resume_id'])
        if not self.request.user.check_object_permissions(self.request, resume):
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )
        return InterestModel.objects.filter(resume_id=resume.id)


class GetInterestDetailsAPIView(CustomRetrieveAPIView):
    queryset = InterestModel.objects.all()
    serializer_class = InterestModelSerializer.List

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


class CreateInterestAPIView(CustomCreateAPIView):
    queryset = InterestModel.objects.all()
    serializer_class = InterestModelSerializer.Write

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


class UpdateInterestDetailsAPIView(CustomUpdateAPIView):
    queryset = InterestModel.objects.all()
    serializer_class = InterestModelSerializer.Write

    def update(self, request, *args, **kwargs):
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
