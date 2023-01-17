from django.contrib.auth import authenticate

from rest_framework import serializers

from user_control.models import UserModel


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
		print(data)
		password = data.get("password", "")
		password2 = data.pop("password2", "")
		is_applicant = data.get("is_applicant", "")
		is_organization = data.get("is_organization", "")
		name = data.get("name", "")

		if name is None:
			raise serializers.ValidationError("Name is required.")
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
		first_name = validated_data.pop("first_name", "")
		last_name = validated_data.pop("last_name", "")
		name = validated_data.pop("name", "")
		if is_applicant:
			print(validated_data)
			print(first_name)
			print(last_name)
			user = UserModel.objects.create_applicant(**validated_data, first_name=first_name, last_name=last_name)
		elif is_organization:
			user = UserModel.objects.create_organization(**validated_data, name=name)
		return user


class LoginSerializer(serializers.Serializer):
	email = serializers.CharField()
	password = serializers.CharField()

	def validate(self, data):
		email = data.get("email", "")
		password = data.get("password", "")

		if email and password:
			user = authenticate(email=email, password=password)
			if user:
				if user.is_active:
					data["user"] = user
				else:
					msg = "User is deactivated."
					raise serializers.ValidationError(msg)
			else:
				msg = "Email or password is incorrect."
				raise serializers.ValidationError(msg)
		else:
			msg = "Must provide email and password both."
			raise serializers.ValidationError(msg)
		return data


class AuthTokenSerializer(serializers.Serializer):
	email = serializers.CharField()
	password = serializers.CharField()

	def validate(self, data):
		email = data.get("email", "")
		password = data.get("password", "")

		if email and password:
			user = authenticate(email=email, password=password)
			if user:
				if user.is_active:
					data["user"] = user
				else:
					msg = "User is deactivated."
					raise serializers.ValidationError(msg)
			else:
				msg = "Email or password is incorrect."
				raise serializers.ValidationError(msg)
		else:
			msg = "Must provide email and password both."
			raise serializers.ValidationError(msg)
		return data

		