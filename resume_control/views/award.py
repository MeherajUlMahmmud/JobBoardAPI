from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination
from resume_control.models import AwardModel
from resume_control.serializers.award import AwardModelSerializer


class AwardModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = AwardModel.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AwardModelSerializer.Write
        return AwardModelSerializer.List
