from django.contrib import admin
from .models import *


class UserModelAdmin(admin.ModelAdmin):
	list_display = ('email', 'is_applicant', 'is_organization', 'is_staff', 'is_active', 'is_superuser')
	list_filter = ('is_applicant', 'is_organization', 'is_staff', 'is_active', 'is_superuser')
	ordering = ('created_at',)


class ApplicantModelAdmin(admin.ModelAdmin):
	list_display = ('user', 'first_name', 'last_name', 'profile_picture', 'phone_number', 'resume')
	ordering = ('created_at',)


class OrganizationModelAdmin(admin.ModelAdmin):
	list_display = ('user', 'name', 'company_logo', 'cover_picture', 'phone_number', 'website', 'description')
	ordering = ('created_at',)


admin.site.register(UserModel, UserModelAdmin)
admin.site.register(ApplicantModel, ApplicantModelAdmin)
admin.site.register(OrganizationModel, OrganizationModelAdmin)
