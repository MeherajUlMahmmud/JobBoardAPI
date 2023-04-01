from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from common.custom_pagination import CustomPageNumberPagination
from resume_control.custom_filters import ResumeModelFilter
from resume_control.models import ResumeModel, PersonalModel, ContactModel
from resume_control.serializers.contact import ContactModelSerializer
from resume_control.serializers.personal import PersonalModelSerializer
from resume_control.serializers.resume import ResumeModelSerializer


class ResumeModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options', 'post', 'put', 'patch', 'delete']
    queryset = ResumeModel.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_class = ResumeModelFilter

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return ResumeModelSerializer.Write
        return ResumeModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        resume = ResumeModel.objects.filter(uuid=instance.uuid).first()

        resume_serializer_data = ResumeModelSerializer.List(resume).data

        personal = PersonalModel.objects.filter(resume=resume.uuid).first()
        personal_serializer_data = PersonalModelSerializer(personal).data
        resume_serializer_data['personal'] = personal_serializer_data

        contact = ContactModel.objects.filter(resume=resume.uuid).first()
        contact_serializer_data = ContactModelSerializer(contact).data
        resume_serializer_data['contact'] = contact_serializer_data

        return Response(resume_serializer_data)
