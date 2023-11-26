from django.utils import timezone
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination


class CustomModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def perform_create(self, serializer):
        serializer.save(
            created_at=timezone.now()
        )

    def perform_update(self, serializer):
        serializer.save(
            updated_at=timezone.now()
        )


class CustomListAPIView(ListAPIView):
    http_method_names = ['get', 'head', 'options']
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination


class CustomRetrieveAPIView(RetrieveAPIView):
    http_method_names = ['get', 'head', 'options']
    permission_classes = [IsAuthenticated]


class CustomCreateAPIView(CreateAPIView):
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination


class CustomUpdateAPIView(UpdateAPIView):
    http_method_names = ['put', 'patch']
    permission_classes = [IsAuthenticated]


class CustomDestroyAPIView(DestroyAPIView):
    http_method_names = ['delete']
    permission_classes = [IsAuthenticated]
