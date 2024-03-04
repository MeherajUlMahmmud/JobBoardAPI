from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.response import Response

from common.custom_view import (
    CustomCreateAPIView, CustomRetrieveAPIView, CustomListAPIView, CustomDestroyAPIView, CustomUpdateAPIView,
)
from resume_control.custom_filters import ResumeModelFilter
from resume_control.models import ResumeModel, PersonalModel, ContactModel
from resume_control.serializers.contact import ContactModelSerializer
from resume_control.serializers.personal import PersonalModelSerializer
from resume_control.serializers.resume import ResumeModelSerializer
from user_control.models import ApplicantModel


class GetResumeListAPIView(CustomListAPIView):
    serializer_class = ResumeModelSerializer.List
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['username', 'email', 'first_name', 'last_name']
    filterset_class = ResumeModelFilter

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ResumeModel.objects.filter(user=self.request.user)
        return ResumeModel.objects.none()


class GetResumeDetailsAPIView(CustomRetrieveAPIView):
    queryset = ResumeModel.objects.all()
    serializer_class = ResumeModelSerializer.List

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.check_object_permissions(request, instance):
            return Response({'detail': 'You do not have permission to perform this action.'}, status=403)

        resume_data = ResumeModelSerializer.List(instance).data
        return Response({
            'data': resume_data,
        }, status=status.HTTP_200_OK)


class CreateResumeAPIView(CustomCreateAPIView):
    serializer_class = ResumeModelSerializer.Write
    queryset = ResumeModel.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        current_user = request.user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        resume = serializer.save(
            user=current_user,
            created_by=current_user,
        )
        applicant = ApplicantModel.objects.get(user=current_user)
        PersonalModel.objects.create(
            resume=resume,
            first_name=applicant.first_name,
            last_name=applicant.last_name,
            created_by=current_user,
        )
        ContactModel.objects.create(
            resume=resume,
            email=resume.user.email,
            created_by=current_user,
        )
        resume_data = ResumeModelSerializer.List(resume).data
        return Response(resume_data, status=status.HTTP_201_CREATED)


class UpdateResumeAPIView(CustomUpdateAPIView):
    queryset = ResumeModel.objects.all()
    serializer_class = ResumeModelSerializer.Write

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.check_object_permissions(request, instance):
            return Response({
                'detail': 'You do not have permission to perform this action.',
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            updated_by=request.user
        )
        resume_data = ResumeModelSerializer.List(instance).data
        return Response(resume_data, status=status.HTTP_200_OK)

class DestroyResumeAPIView(CustomDestroyAPIView):
    queryset = ResumeModel.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.check_object_permissions(request, instance):
            return Response({
                'detail': 'You do not have permission to perform this action.',
            }, status=status.HTTP_403_FORBIDDEN)

        personal = instance.personal
        print(personal)
        contact = instance.contact
        print(contact)
        educations = instance.education.all()
        print("Educations length: ", len(educations))
        experiences = instance.experience.all()
        print("Experiences length: ", len(experiences))
        # skills = instance.skill_set.all()
        # languages = instance.language_set.all()
        # interests = instance.interest_set.all()
        # awards = instance.award_set.all()
        # certifications = instance.certification_set.all()
        # references = instance.reference_set.all()
        return Response(status=status.HTTP_204_NO_CONTENT)
