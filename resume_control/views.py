from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from resume_control.serializers import *


class ExperienceAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        experience_id = request.GET.get('experience_id')
        if experience_id:
            experience = ExperienceModel.objects.get(uuid=experience_id, user=request.user)
            serializer = ExperienceModelGetSerializer(experience)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            experiences = ExperienceModel.objects.filter(user=request.user)
            serializer = ExperienceModelGetSerializer(experiences, many=True)
            return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = ExperienceModelPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @staticmethod  # static method is used to avoid passing self as a parameter
    def put(request):
        experience_id = request.GET.get('experience_id')
        if experience_id:
            experience = ExperienceModel.objects.get(uuid=experience_id, user=request.user)
            serializer = ExperienceModelPostSerializer(experience, data=request.data)
            if serializer.is_valid():
                serializer.update(experience, serializer.validated_data)
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'experience_id is required'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        experience_id = request.GET.get('experience_id')
        if experience_id:
            experience = ExperienceModel.objects.get(uuid=experience_id, user=request.user)
            experience.delete()
            return Response({'success': 'Experience deleted successfully'}, status=HTTP_200_OK)
        else:
            return Response({'error': 'experience_id is required'}, status=HTTP_400_BAD_REQUEST)


class EducationAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        education_id = request.GET.get('education_id')
        if education_id:
            education = EducationModel.objects.get(uuid=education_id, user=request.user)
            serializer = EducationModelGetSerializer(education)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            educations = EducationModel.objects.filter(user=request.user)
            serializer = EducationModelGetSerializer(educations, many=True)
            return Response(serializer.data, status=HTTP_200_OK)

    @staticmethod
    def post(request):
        pass

    @staticmethod
    def put(request):
        education_id = request.GET.get('education_id')
        if education_id:
            education = EducationModel.objects.get(uuid=education_id, user=request.user)
            serializer = EducationModelPostSerializer(education, data=request.data)
            if serializer.is_valid():
                serializer.update(education, serializer.validated_data)
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'education_id is required'}, status=HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        education_id = request.GET.get('education_id')
        if education_id:
            education = EducationModel.objects.get(uuid=education_id, user=request.user)
            education.delete()
            return Response({'success': 'Education deleted successfully'}, status=HTTP_200_OK)
        else:
            return Response({'error': 'education_id is required'}, status=HTTP_400_BAD_REQUEST)


class SkillAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        pass

    @staticmethod
    def post(request):
        pass

    @staticmethod
    def put(request):
        pass

    @staticmethod
    def delete(request):
        pass


class LanguageAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        pass

    @staticmethod
    def post(request):
        pass

    @staticmethod
    def put(request):
        pass

    @staticmethod
    def delete(request):
        pass


class InterestAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        pass

    @staticmethod
    def post(request):
        pass

    @staticmethod
    def put(request):
        pass

    @staticmethod
    def delete(request):
        pass


class ReferenceAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        pass

    @staticmethod
    def post(request):
        pass

    @staticmethod
    def put(request):
        pass

    @staticmethod
    def delete(request):
        pass


class AwardAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        pass

    @staticmethod
    def post(request):
        pass

    @staticmethod
    def put(request):
        pass

    @staticmethod
    def delete(request):
        pass


class CertificationAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        pass

    @staticmethod
    def post(request):
        pass

    @staticmethod
    def put(request):
        pass

    @staticmethod
    def delete(request):
        pass
