import os

import jwt
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponsePermanentRedirect
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

from .serializers import (LoginSerializer, RegisterSerializer, EmailVerificationSerializer,
                          ResendVerificationEmailSerializer, LogoutSerializer)
from .utils import Util


class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


class RegisterAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    @transaction.atomic
    def post(self, request):
        try:
            data = request.data
            print(data)
            is_applicant = data.get('is_applicant')
            is_organization = data.get('is_organization')
            name = request.data.get('name')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')

            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            user_data = serializer.data
            user = UserModel.objects.get(email=user_data['email'])
            if is_applicant:
                applicant = ApplicantModel.objects.create(user=user, first_name=first_name, last_name=last_name)
                applicant.save()
            elif is_organization:
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

            return Response({'data': user_data, 'message': 'User created successfully'},
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
            user = UserModel.objects.get(uuid=payload['user_uuid'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'message': 'Email successfully verified'},
                            status=HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=HTTP_400_BAD_REQUEST)


class ResendVerificationEmailAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ResendVerificationEmailSerializer

    def post(self, request):
        data = request.data
        email = data.get('email')
        if email is None:
            return Response({'error': 'Please provide an email address'}, status=HTTP_400_BAD_REQUEST)
        user = UserModel.objects.get(email=email)
        if user:
            if user.is_verified:
                return Response({'error': 'Email already verified'}, status=HTTP_400_BAD_REQUEST)

            if user.is_applicant:
                applicant = ApplicantModel.objects.get(user=user)
            elif user.is_organization:
                organization = OrganizationModel.objects.get(user=user)

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

            return Response({'message': 'Email sent successfully'}, status=HTTP_200_OK)
        return Response({'error': 'User does not exist'}, status=HTTP_400_BAD_REQUEST)


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
            return Response({'user': user_data, 'tokens': tokens }, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# class RequestPasswordResetEmail(GenericAPIView):
#     serializer_class = ResetPasswordEmailRequestSerializer
#
#     def post(self, request):
#         data = request.data
#         serializer = self.serializer_class(data=data)
#
#         email = data.get('email', '')
#
#         user = UserModel.objects.get(email=email)
#         if user:
#             user = UserModel.objects.get(email=email)
#             uidb64 = urlsafe_base64_encode(smart_bytes(user.uuid))
#             token = PasswordResetTokenGenerator().make_token(user)
#             current_site = get_current_site(request).domain
#             relative_link = reverse(
#                 'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
#
#             redirect_url = request.data.get('redirect_url', '')
#             abs_url = 'http://' + current_site + relative_link
#             email_body = 'Hello,\nUse link below to reset your password\n' + \
#                          abs_url + "?redirect_url=" + redirect_url
#             data = {'email_body': email_body, 'to_email': user.email,
#                     'email_subject': 'Reset your password'}
#             Util.send_email(data)
#             return Response({'success': 'We have sent you a link to reset your password'}, status=HTTP_200_OK)
#         return Response({'error': 'User does not exist'}, status=HTTP_400_BAD_REQUEST)
#
#
# class PasswordTokenCheckAPI(GenericAPIView):
#     serializer_class = SetNewPasswordSerializer
#
#     def get(self, request, uidb64, token):
#         redirect_url = request.GET.get('redirect_url')
#
#         try:
#             uuid = smart_str(urlsafe_base64_decode(uidb64))
#             user = UserModel.objects.get(uuid=uuid)
#
#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 if len(redirect_url) > 3:
#                     return CustomRedirect(redirect_url + '?token_valid=False')
#                 else:
#                     return CustomRedirect(os.environ.get('FRONTEND_URL', '') + '?token_valid=False')
#
#             if redirect_url and len(redirect_url) > 3:
#                 return CustomRedirect(
#                     redirect_url + '?token_valid=True&message=Credentials Valid&uidb64=' + uidb64 + '&token=' + token)
#             else:
#                 return CustomRedirect(os.environ.get('FRONTEND_URL', '') + '?token_valid=False')
#
#         except DjangoUnicodeDecodeError as identifier:
#             try:
#                 if not PasswordResetTokenGenerator().check_token(user):
#                     return CustomRedirect(redirect_url + '?token_valid=False')
#
#             except UnboundLocalError as e:
#                 return Response({'error': 'Token is not valid, please request a new one'},
#                                 status=HTTP_400_BAD_REQUEST)
#
#
# class SetNewPasswordAPIView(GenericAPIView):
#     serializer_class = SetNewPasswordSerializer
#
#     def patch(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response({'success': True, 'message': 'Password reset success'}, status=HTTP_200_OK)


class LogoutAPIView(GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=HTTP_204_NO_CONTENT)

# class ObtainAuthToken(APIView):
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         # token = Token.objects.get_or_create(user=user)[0]
#         # if user:
#         #     return Response({"token": token.key}, status=HTTP_200_OK)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
