from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from common.custom_permissions import AdminOrOrganizationPermission, AdminOrStaffUserPermission
from common.custom_view import (
    CustomListAPIView, CustomCreateAPIView, CustomRetrieveAPIView, CustomUpdateAPIView, CustomDestroyAPIView,
)
from test_control.custom_filters import OptionModelFilter
from test_control.models import OptionModel, QuestionModel
from test_control.serializers.option import OptionModelSerializer


class GetOptionListAPIView(CustomListAPIView):
    queryset = OptionModel.objects.filter(is_active=True, is_deleted=False)
    permission_classes = [AdminOrStaffUserPermission]
    serializer_class = OptionModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['text', ]
    filterset_class = OptionModelFilter


class GetOptionListByQuestionAPIView(CustomListAPIView):
    queryset = OptionModel.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['text', ]
    filterset_class = OptionModelFilter

    def get_serializer_class(self):
        requested_user = self.request.user
        if requested_user.is_applicant:
            return OptionModelSerializer.DetailsForExamine
        else:
            return OptionModelSerializer.List

    def get(self, request, *args, **kwargs):
        question = get_object_or_404(QuestionModel, id=self.kwargs['question_id'])

        if not self.request.user.check_object_permissions(self.request, question):
            return Response(
                {'detail': 'You do not have permission to perform this action.'},
                status=HTTP_403_FORBIDDEN
            )

        queryset = OptionModel.objects.filter(
            question=question, is_active=True, is_deleted=False,
        )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class CreateOptionAPIView(CustomCreateAPIView):
    queryset = OptionModel.objects.all()
    permission_classes = [AdminOrOrganizationPermission]
    serializer_class = OptionModelSerializer.Write

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        question = get_object_or_404(
            QuestionModel,
            id=request.data['question'], is_active=True, is_deleted=False,
        )

        if not self.request.user.check_object_permissions(self.request, question):
            return Response(
                {'detail': 'You are not allowed to perform this action.'},
                status=HTTP_403_FORBIDDEN,
            )

        serializer.save(created_by=request.user)
        return Response(serializer.data, status=HTTP_200_OK)


class GetOptionDetailsAPIView(CustomRetrieveAPIView):
    queryset = OptionModel.objects.all()

    def get_serializer_class(self):
        requested_user = self.request.user
        if requested_user.is_applicant:
            return OptionModelSerializer.DetailsForExamine
        else:
            return OptionModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class UpdateOptionDetailsAPIView(CustomUpdateAPIView):
    queryset = OptionModel.objects.all()
    permission_classes = [AdminOrOrganizationPermission]
    serializer_class = OptionModelSerializer.Write

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        if not self.request.user.check_object_permissions(self.request, instance):
            return Response(
                {'detail': 'You are not allowed to perform this action.'},
                status=HTTP_403_FORBIDDEN,
            )

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(updated_by=request.user)
        return Response(serializer.data, status=HTTP_200_OK)


class DeleteOptionAPIView(CustomDestroyAPIView):
    queryset = OptionModel.objects.all()
    permission_classes = [AdminOrOrganizationPermission]
    serializer_class = OptionModelSerializer.List

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        if not self.request.user.check_object_permissions(self.request, instance):
            return Response(
                {'detail': 'You are not allowed to perform this action.'},
                status=HTTP_403_FORBIDDEN,
            )

        instance.delete()
        return Response({'detail': 'Option deleted successfully.'}, status=HTTP_200_OK)
