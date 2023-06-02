from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from resume_control.custom_filters import ContactModelFilter
from resume_control.models import ContactModel
from resume_control.serializers.contact import ContactModelSerializer


class ContactModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = ContactModel.objects.all().order_by('-created_at')
    serializer_class = ContactModelSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = ContactModelFilter
