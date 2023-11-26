from django.contrib.auth import authenticate

from rest_framework.serializers import (
    Serializer, ModelSerializer, CharField, BooleanField, EmailField, ValidationError,
)
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from user_control.models import UserModel, ApplicantModel, OrganizationModel


class RegisterSerializer(ModelSerializer):
    name = CharField(max_length=255, min_length=3, required=False)
    first_name = CharField(max_length=255, min_length=3, required=False)
    last_name = CharField(max_length=255, min_length=3, required=False)
    password = CharField(write_only=True)
    password2 = CharField(write_only=True)
    is_applicant = BooleanField(required=True)
    is_organization = BooleanField(required=True)

    class Meta:
        model = UserModel
        fields = [
            'id',
            'name',
            'first_name',
            'last_name',
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
            raise ValidationError("Passwords must match.")

        if is_applicant and is_organization:
            raise ValidationError("User can't be both student and teacher.")

        if not is_applicant and not is_organization:
            raise ValidationError("User must be either student or teacher.")

        return data

    def create(self, validated_data):
        is_applicant = validated_data.pop("is_applicant", "")
        is_organization = validated_data.pop("is_organization", "")

        if is_applicant:
            user = UserModel.objects.create_applicant(**validated_data)
            return user
        elif is_organization:
            user = UserModel.objects.create_organization(**validated_data)
            return user
        else:
            raise ValidationError("User must be either applicant or organization.")


class EmailVerificationSerializer(ModelSerializer):
    token = CharField(max_length=555)

    class Meta:
        model = UserModel
        fields = ['token']


class ResendVerificationEmailSerializer(ModelSerializer):
    email = EmailField(max_length=255, min_length=3)

    class Meta:
        model = UserModel
        fields = ['email']


class LoginSerializer(Serializer):
    email = EmailField(max_length=255, min_length=3)
    password = CharField(write_only=True)

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
            #     raise AuthenticationFailed('Account is not verified')

            return {
                'user': user,
                'tokens': user.tokens()
            }
        else:
            msg = "Must provide email and password both."
            raise ValidationError(msg)


class ResetPasswordRequestSerializer(Serializer):
    email = EmailField(min_length=2)

    class Meta:
        fields = [
            'email',
        ]


class SetNewPasswordSerializer(Serializer):
    password1 = CharField(min_length=6, max_length=68, write_only=True)
    password2 = CharField(min_length=6, max_length=68, write_only=True)

    class Meta:
        fields = [
            'password1',
            'password2',
        ]

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise ValidationError('Passwords do not match')
        return attrs


class LogoutSerializer(Serializer):
    refresh = CharField()

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
