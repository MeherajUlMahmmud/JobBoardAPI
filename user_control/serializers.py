from rest_framework import serializers

from .models import *


class UserModelSerializer(serializers.ModelSerializer):
	applicant = serializers.SerializerMethodField()
	organization = serializers.SerializerMethodField()

	class Meta:
		model = UserModel
		fields = [
			'uuid',
			'email',
			'applicant',
			'organization',
			'is_applicant',
			'is_organization',
			'is_staff',
			'is_superuser',
		]

	def get_applicant(self, obj):
		if obj.is_applicant:
			return ApplicantModelSerializer(obj.applicant).data
		return None

	def get_organization(self, obj):
		if obj.is_organization:
			return OrganizationModelSerializer(obj.organization).data
		return None


class ApplicantModelSerializer(serializers.ModelSerializer):
	# user = serializers.SerializerMethodField()

	class Meta:
		model = ApplicantModel
		fields = [
			'uuid',
			# 'user',
			'first_name',
			'last_name',
			'profile_picture',
			'phone_number',
			'resume',
		]

	# def get_user(self, obj):
	# 	return UserModelSerializer(obj.user).data


class OrganizationModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrganizationModel
		fields = [
			'uuid',
			'name',
			'company_logo',
			'cover_picture',
			'phone_number',
			'website',
			'description',
		]
