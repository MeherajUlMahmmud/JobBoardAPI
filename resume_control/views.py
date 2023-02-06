from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from resume_control.models import *
from resume_control.serializers import *


class ExperienceAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class EducationAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class SkillAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class LanguageAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class InterestAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class ReferenceAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class AwardAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class CertificationAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
