from django.db import models
from django.db.models import Count
from django.db.models.functions import Coalesce
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK

from common.custom_permissions import AdminOrOrganizationPermission
from common.custom_view import (
    CustomListAPIView, CustomCreateAPIView, CustomUpdateAPIView, CustomRetrieveAPIView,
)
from test_control.custom_filters import ExamModelFilter
from test_control.models import ExamModel
from test_control.serializers.exam import ExamModelSerializer


class GetExamListAPIView(CustomListAPIView):
    permission_classes = [AdminOrOrganizationPermission]
    serializer_class = ExamModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = ExamModelFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_admin or user.is_staff or user.is_superuser:
            queryset = ExamModel.objects.all().prefetch_related(
                'questions',
            ).annotate(
                total_questions=Coalesce(
                    Count(
                        'questions__id', output_field=models.IntegerField(),
                    ),  #
                    0,  #
                ),
            )
            return queryset
        elif user.is_organization:
            queryset = ExamModel.objects.filter(
                created_by=user, is_active=True, is_deleted=False,
            ).prefetch_related(
                'questions',
            ).annotate(
                total_questions=Coalesce(
                    Count(
                        'questions__id', output_field=models.IntegerField(),
                    ),  #
                    0,  #
                ),
            )
            return queryset


class CreateExamAPIView(CustomCreateAPIView):
    queryset = ExamModel.objects.all()
    permission_classes = [AdminOrOrganizationPermission]
    serializer_class = ExamModelSerializer.Write

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            created_by=request.user,
        )
        return Response({'detail': 'Exam created successfully.'}, status=HTTP_200_OK)


class GetExamDetailsAPIView(CustomRetrieveAPIView):
    queryset = ExamModel.objects.all()
    serializer_class = ExamModelSerializer.Details

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if (request.user.is_organization and instance.created_by == request.user) or request.user.is_admin:
            exam = ExamModel.objects.filter(
                id=instance.id, is_active=True, is_deleted=False,
            ).prefetch_related(
                'questions',
            ).annotate(
                total_questions=Coalesce(
                    Count(
                        'questions__id', output_field=models.IntegerField(),
                    ),
                    0,
                ),
            )

            serializer = ExamModelSerializer.Details(exam.first())
            return Response(serializer.data, status=HTTP_200_OK)
        elif request.user.is_applicant:
            exam = ExamModel.objects.filter(
                id=instance.id, is_active=True, is_deleted=False,
            ).prefetch_related(
                'questions',
            ).annotate(
                total_questions=Coalesce(
                    Count(
                        'questions__id', output_field=models.IntegerField(),
                    ),
                    0,
                ),
            )

            serializer = ExamModelSerializer.DetailsForExamine(exam.first())
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response({'detail': 'You are not allowed to view this exam.'}, status=HTTP_403_FORBIDDEN)


class UpdateExamAPIView(CustomUpdateAPIView):
    queryset = ExamModel.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ExamModelSerializer.Write

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.is_organization and instance.created_by != request.user:
            return Response(
                {'detail': 'You don\'t have permission to perform this action.'},
                status=HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)
