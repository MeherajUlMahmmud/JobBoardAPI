from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination
from user_control.custom_filters import ApplicantModelFilter
from user_control.models import ApplicantModel
from user_control.serializers.applicant import ApplicantModelSerializer


class ApplicantModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'put', 'patch', 'delete']
    queryset = ApplicantModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filterset_class = ApplicantModelFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ApplicantModelSerializer.List
        return ApplicantModelSerializer.Write
