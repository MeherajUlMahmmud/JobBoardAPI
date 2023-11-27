import os
from datetime import timedelta, datetime

import jwt
import pytz
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.encoding import smart_bytes, smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework_simplejwt.tokens import RefreshToken

from user_control.models import ApplicantModel, OrganizationModel, UserModel
from user_control.serializers.user import UserModelSerializer

from .serializers import (
    LoginSerializer, RegisterSerializer, EmailVerificationSerializer, ResendVerificationEmailSerializer,
    LogoutSerializer, ResetPasswordRequestSerializer, SetNewPasswordSerializer,
)
from .utils import Util


class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


class RegisterAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    @transaction.atomic
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            print(data)

            name = data.get('name')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password')
            is_applicant = data.get('is_applicant')
            is_organization = data.get('is_organization')

            if is_applicant:
                user = UserModel.objects.create_applicant(email=email, password=password)
                applicant = ApplicantModel.objects.create(user=user, first_name=first_name, last_name=last_name)
                applicant.save()
            elif is_organization:
                user = UserModel.objects.create_organization(email=email, password=password)
                organization = OrganizationModel.objects.create(user=user, name=name)
                organization.save()

            # name = applicant.first_name + " " + applicant.last_name if is_applicant else organization.name
            # token = RefreshToken.for_user(user).access_token
            #
            # current_site = get_current_site(request).domain
            # relative_link = reverse('verify-email')
            # abs_url = 'http://' + current_site + relative_link + "?token=" + str(token)
            #
            # email_subject = 'Verify your email'
            # email_body = "Hi " + name + ",\nUse this link to verify your email:\n" + abs_url
            # email_data = {
            #     'email_subject': email_subject,
            #     'email_body': email_body,
            #     'to_email_list': [user.email],
            # }
            # # Util.send_email(email_data)
            # send_mail(
            #     email_data['email_subject'],
            #     email_data['email_body'],
            #     'gktournament64@gmail.com',
            #     email_data['to_email_list'],
            #     fail_silently=False,
            # )

            return Response({'message': 'User created successfully'},
                            status=HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)


class VerifyEmailAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = get_object_or_404(UserModel, id=payload['user_id'])

            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response({'detail': 'Email successfully verified'},
                            status=HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'detail': 'Activation Expired'}, status=HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'detail': 'Invalid token'}, status=HTTP_400_BAD_REQUEST)


class ResendVerificationEmailAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ResendVerificationEmailSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        email = data.get('email')
        if email is None:
            return Response({'detail': 'Please provide an email address'}, status=HTTP_400_BAD_REQUEST)
        user = get_object_or_404(UserModel, email=email)

        if user.is_verified:
            return Response({'detail': 'Email already verified'}, status=HTTP_400_BAD_REQUEST)

        if user.is_applicant:
            applicant = ApplicantModel.objects.get(user=user, created_by=user)
        elif user.is_organization:
            organization = OrganizationModel.objects.get(user=user, created_by=user)

        name = applicant.first_name + " " + applicant.last_name if user.is_applicant else organization.name
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_link = reverse('verify-email')
        abs_url = 'http://' + current_site + relative_link + "?token=" + str(token)

        email_subject = 'Verify your email'
        email_body = "Hi " + name + ",\nUse this link to verify your email:\n" + abs_url
        email_data = {
            'email_subject': email_subject,
            'email_body': email_body,
            'to_email': user.email,
        }
        Util.send_email(email_data)

        return Response({'detail': 'Email sent successfully'}, status=HTTP_200_OK)


class LoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        tokens = serializer.validated_data['tokens']
        if user:
            user_data = UserModelSerializer.List(user).data
            return Response({'user': user_data, 'tokens': tokens}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=HTTP_204_NO_CONTENT)


class PasswordChangeAPIView(GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user.set_password(serializer.validated_data['password1'])
        user.save()
        return Response({'detail': 'Password changed successfully'}, status=HTTP_200_OK)


class RequestPasswordResetAPIView(GenericAPIView):
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        email = data.get('email')

        user = get_object_or_404(UserModel, email=email)

        u_id_b64 = urlsafe_base64_encode(smart_bytes(user.id) + smart_bytes('||') + smart_bytes(user.email))
        token = PasswordResetTokenGenerator().make_token(user)

        user.reset_password_token = token
        user.reset_password_token_expiry = datetime.now() + timedelta(minutes=5)
        user.save()

        return Response({'u_id_b64': u_id_b64, 'token': token}, status=HTTP_200_OK)

        # current_site = get_current_site(request).domain
        # relative_link = reverse(
        #     'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
        #
        # redirect_url = request.data.get('redirect_url', '')
        # abs_url = 'http://' + current_site + relative_link
        # email_body = 'Hello,\nUse link below to reset your password\n' + \
        #              abs_url + "?redirect_url=" + redirect_url
        # data = {'email_body': email_body, 'to_email': user.email,
        #         'email_subject': 'Reset your password'}
        # Util.send_email(data)
        # return Response({'success': 'We have sent you a link to reset your password'}, status=HTTP_200_OK)


class PasswordResetAPIView(GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def post(self, request, uidb64, token):
        utc = pytz.UTC

        try:
            user_data_str = smart_str(urlsafe_base64_decode(uidb64))
            user_id = int(user_data_str.split('||')[0])
            user_email = user_data_str.split('||')[1]
            user = get_object_or_404(UserModel, id=user_id, email=user_email)
            if not user.reset_password_token == token:
                return Response({'detail': 'Token does not match, please request a new one'},
                                status=HTTP_400_BAD_REQUEST)
            if not user.reset_password_token_expiry.replace(tzinfo=utc) < datetime.now().replace(tzinfo=utc):
                return Response({'detail': 'Token expired, please request a new one'},
                                status=HTTP_400_BAD_REQUEST)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'detail': 'Token is not valid, please request a new one'},
                                status=HTTP_400_BAD_REQUEST)

            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            user.set_password(serializer.validated_data['password1'])
            user.reset_password_token = None
            user.reset_password_token_expiry = None
            user.save()

            return Response({'detail': 'Password reset successfully'}, status=HTTP_200_OK)
        except DjangoUnicodeDecodeError as identifier:
            return Response({'detail': 'Token is not valid, please request a new one'},
                            status=HTTP_400_BAD_REQUEST)
