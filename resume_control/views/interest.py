from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from resume_control.custom_filters import InterestModelFilter
from resume_control.models import InterestModel
from resume_control.serializers.interest import InterestModelSerializer


class InterestModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = InterestModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_class = InterestModelFilter

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return InterestModelSerializer.Write
        return InterestModelSerializer.List
