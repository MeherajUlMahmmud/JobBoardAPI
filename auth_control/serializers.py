from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from user_control.models import UserModel, ApplicantModel, OrganizationModel


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    is_applicant = serializers.BooleanField(required=True)
    is_organization = serializers.BooleanField(required=True)

    class Meta:
        model = UserModel
        fields = [
            'uuid',
            'email',
            'password',
            'password2',
            "is_applicant",
            "is_organization",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        password = data.get("password", "")
        password2 = data.pop("password2", "")
        is_applicant = data.get("is_applicant", "")
        is_organization = data.get("is_organization", "")

        if password != password2:
            raise serializers.ValidationError("Passwords must match.")

        if is_applicant and is_organization:
            raise serializers.ValidationError("User can't be both student and teacher.")

        if not is_applicant and not is_organization:
            raise serializers.ValidationError("User must be either student or teacher.")

        return data

    def create(self, validated_data):
        is_applicant = validated_data.pop("is_applicant", "")
        is_organization = validated_data.pop("is_organization", "")

        if is_applicant:
            user = UserModel.objects.create_applicant(**validated_data)
        elif is_organization:
            user = UserModel.objects.create_organization(**validated_data)
        return user


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = UserModel
        fields = ['token']


class ResendVerificationEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)

    class Meta:
        model = UserModel
        fields = ['email']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    def validate(self, data):
        email = data.get("email", "")
        password = data.get("password", "")

        if email and password:
            user = authenticate(email=email, password=password)

            if not user:
                raise AuthenticationFailed('Invalid credentials, try again')
            if not user.is_active:
                raise AuthenticationFailed('Account disabled, contact admin')
            # if not user.is_verified:
            #     raise AuthenticationFailed('Email is not verified')

            return {
                'user': user,
                'tokens': user.tokens()
            }
        else:
            msg = "Must provide email and password both."
            raise serializers.ValidationError(msg)


# class ResetPasswordEmailRequestSerializer(serializers.Serializer):
#     email = serializers.EmailField(min_length=2)
#
#     redirect_url = serializers.CharField(max_length=500, required=False)
#
#     class Meta:
#         fields = ['email']
#
#
# class SetNewPasswordSerializer(serializers.Serializer):
#     password = serializers.CharField(min_length=6, max_length=68, write_only=True)
#     token = serializers.CharField(min_length=1, write_only=True)
#     uidb64 = serializers.CharField(min_length=1, write_only=True)
#
#     class Meta:
#         fields = ['password', 'token', 'uidb64']
#
#     def validate(self, attrs):
#         try:
#             password = attrs.get('password')
#             token = attrs.get('token')
#             uidb64 = attrs.get('uidb64')
#
#             uuid = force_str(urlsafe_base64_decode(uidb64))
#             user = UserModel.objects.get(uuid=uuid)
#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 raise AuthenticationFailed('The reset link is invalid', 401)
#
#             user.set_password(password)
#             user.save()
#
#             return user
#         except Exception as e:
#             raise AuthenticationFailed('The reset link is invalid', 401)
#         return super().validate(attrs)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': 'Token is expired or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
