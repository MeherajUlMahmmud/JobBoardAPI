from django.db import models
from django.db.models import Count
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from common.custom_permissions import AdminOrOrganizationPermission, AdminOrStaffUserPermission
from common.custom_view import (
    CustomListAPIView, CustomCreateAPIView, CustomRetrieveAPIView, CustomUpdateAPIView,
)
from test_control.custom_filters import QuestionModelFilter
from test_control.models import QuestionModel, ExamModel
from test_control.serializers.question import QuestionModelSerializer


class GetQuestionListAPIView(CustomListAPIView):
    permission_classes = [AdminOrStaffUserPermission]
    serializer_class = QuestionModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['prompt']
    filterset_class = QuestionModelFilter

    def get_queryset(self):
        user = self.request.user
        queryset = QuestionModel.objects.filter(
            created_by=user, is_active=True, is_deleted=False,
        ).prefetch_related(
            'options',
        ).annotate(
            total_options=Coalesce(
                Count(
                    'options__id', output_field=models.IntegerField(),
                ),
                0,
            ),
        )
        return queryset


class CreateQuestionAPIView(CustomCreateAPIView):
    queryset = QuestionModel.objects.all()
    permission_classes = [AdminOrOrganizationPermission]
    serializer_class = QuestionModelSerializer.Write

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


class GetQuestionListByExamAPIView(CustomListAPIView):
    queryset = QuestionModel.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['prompt']
    filterset_class = QuestionModelFilter

    def get_serializer_class(self):
        requested_user = self.request.user
        if requested_user.is_applicant:
            return QuestionModelSerializer.DetailsForExamine
        else:
            return QuestionModelSerializer.List

    def get_queryset(self):
        exam = get_object_or_404(ExamModel, id=self.kwargs['exam_id'])
        if not self.request.user.check_object_permissions(self.request, exam):
            return Response(
                {
                    'detail': 'You don\'t have permission to perform this action.'
                },
                status=HTTP_403_FORBIDDEN
            )
        queryset = QuestionModel.objects.filter(exam_id=exam.id).prefetch_related(
            'options',
        ).annotate(
            total_options=Coalesce(
                Count(
                    'options__id', output_field=models.IntegerField(),
                ),
                0,
            ),
        )
        return queryset


class GetQuestionDetailsAPIView(CustomRetrieveAPIView):
    queryset = QuestionModel.objects.all()

    def get_serializer_class(self):
        requested_user = self.request.user
        if requested_user.is_applicant:
            return QuestionModelSerializer.DetailsForExamine
        else:
            return QuestionModelSerializer.Details

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class UpdateQuestionAPIView(CustomUpdateAPIView):
    queryset = QuestionModel.objects.all()
    permission_classes = [AdminOrOrganizationPermission]
    serializer_class = QuestionModelSerializer.Write

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


class DeleteQuestionAPIView(CustomUpdateAPIView):
    queryset = QuestionModel.objects.all()
    permission_classes = [AdminOrOrganizationPermission]
    serializer_class = QuestionModelSerializer.Write

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        if not self.request.user.check_object_permissions(self.request, instance):
            return Response(
                {'detail': 'You are not allowed to perform this action.'},
                status=HTTP_403_FORBIDDEN,
            )

        instance.is_active = False
        instance.is_deleted = True
        instance.save()
        return Response({'detail': 'Question deleted successfully.'}, status=HTTP_200_OK)
