from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from common.admin import RawIdFieldsAdmin
from .models import *


@admin.register(UserModel)
class UserModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = (
        'email', 'is_applicant', 'is_organization', 'is_staff', 'is_superuser',
    )
    list_filter = (
        'is_applicant', 'is_organization', 'is_staff', 'is_superuser',
    )
    search_fields = (
        'email',
    )
    readonly_fields = (
        'password',
        'reset_password_token',
        'reset_password_token_expiry',
    )
    fieldsets = (
        (None, {'fields': (
            'email',
            'password', 'reset_password_token', 'reset_password_token_expiry',
            'extra_fields',
        )}),
        ('Permissions', {'fields': (
            'is_applicant', 'is_organization', 'is_staff', 'is_superuser',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )


@admin.register(ApplicantModel)
class ApplicantModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = (
        'user',
        'first_name', 'last_name',
        'phone_number',
    )
    search_fields = (
        'user__email',
        'first_name', 'last_name',
        'phone_number',
    )
    fieldsets = (
        (None, {'fields': (
            'user',
            'first_name', 'last_name',
            'profile_picture', 'phone_number',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )


@admin.register(OrganizationModel)
class OrganizationModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = (
        'user', 'name', 'phone_number', 'website',
    )
    search_fields = (
        'user__email',
        'name', 'phone_number', 'website',
    )
    fieldsets = (
        (None, {'fields': (
            'user',
            'name', 'company_logo', 'cover_picture', 'phone_number', 'website',
            'description', 'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )
