from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.response import Response

from common.custom_view import (
    CustomCreateAPIView, CustomRetrieveAPIView, CustomListAPIView, CustomDestroyAPIView, CustomUpdateAPIView,
)
from resume_control.custom_filters import ResumeModelFilter
from resume_control.models import ResumeModel, PersonalModel, ContactModel
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


class GetResumePreviewAPIView(CustomRetrieveAPIView):
    queryset = ResumeModel.objects.all()
    serializer_class = ResumeModelSerializer.Preview

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.check_object_permissions(request, instance):
            return Response({'detail': 'You do not have permission to perform this action.'}, status=403)

        resume_data = ResumeModelSerializer.Preview(instance).data
        # sort all the inner list according to the serial and filter out the inactive and deleted items
        resume_data['education'] = sorted(
            [education for education in resume_data['education'] if
             education['is_active'] and not education['is_deleted']],
            key=lambda x: x['serial']
        )
        resume_data['experience'] = sorted(
            [experience for experience in resume_data['experience'] if
             experience['is_active'] and not experience['is_deleted']],
            key=lambda x: x['serial']
        )
        resume_data['skill'] = sorted(
            [skill for skill in resume_data['skill'] if
             skill['is_active'] and not skill['is_deleted']],
            key=lambda x: x['serial']
        )
        resume_data['language'] = sorted(
            [language for language in resume_data['language'] if
             language['is_active'] and not language['is_deleted']],
            key=lambda x: x['serial']
        )
        resume_data['interest'] = sorted(
            [interest for interest in resume_data['interest'] if
             interest['is_active'] and not interest['is_deleted']],
            key=lambda x: x['serial']
        )
        resume_data['award'] = sorted(
            [award for award in resume_data['award'] if
             award['is_active'] and not award['is_deleted']],
            key=lambda x: x['serial']
        )
        resume_data['certification'] = sorted(
            [certification for certification in resume_data['certification'] if
             certification['is_active'] and not certification['is_deleted']],
            key=lambda x: x['serial']
        )
        resume_data['reference'] = sorted(
            [reference for reference in resume_data['reference'] if
             reference['is_active'] and not reference['is_deleted']],
            key=lambda x: x['serial']
        )

        return Response(resume_data,
                        status=status.HTTP_200_OK)


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

    @transaction.atomic
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.check_object_permissions(request, instance):
            return Response({
                'detail': 'You do not have permission to perform this action.',
            }, status=status.HTTP_403_FORBIDDEN)

        try:
            personal = instance.personal
            contact = instance.contact
            educations = instance.education.all()
            experiences = instance.experience.all()
            skills = instance.skill.all()
            languages = instance.language.all()
            interests = instance.interest.all()
            awards = instance.award.all()
            # certifications = instance.certification_set.all()
            # references = instance.reference_set.all()

            personal.delete()
            contact.delete()
            for education in educations:
                education.delete()
            for experience in experiences:
                experience.delete()
            for skill in skills:
                skill.delete()
            for language in languages:
                language.delete()
            for interest in interests:
                interest.delete()
            for award in awards:
                award.delete()
            # for certification in certifications:
            #     certification.delete()
            # for reference in references:
            #     reference.delete()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({
                'detail': 'Failed to delete resume.',
            }, status=status.HTTP_400_BAD_REQUEST)
