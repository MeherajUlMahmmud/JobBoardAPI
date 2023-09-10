from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from common.admin import RawIdFieldsAdmin
from resume_control.models import (
    ResumeModel, PersonalModel, ContactModel, ExperienceModel, EducationModel, SkillModel, LanguageModel,
    InterestModel, ReferenceModel, AwardModel, CertificationModel,
)


@admin.register(ResumeModel)
class ResumeModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = [
        'user',
        'name',
        'is_education_visible',
        'is_experience_visible',
        'is_skill_visible',
        'is_language_visible',
        'is_interest_visible',
        'is_reference_visible',
        'is_award_visible',
        'is_certification_visible',
    ]
    list_filter = [
        'user',
    ]
    search_fields = [
        'user',
        'name',
    ]
    fieldsets = (
        (None, {'fields': (
            'user', 'name',
            'extra_fields',
        )}),
        ('Permissions', {'fields': (
            'is_education_visible', 'is_experience_visible', 'is_skill_visible', 'is_language_visible',
            'is_interest_visible', 'is_reference_visible', 'is_award_visible', 'is_certification_visible',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )


@admin.register(PersonalModel)
class PersonalModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = [
        'resume',
        'first_name',
        'last_name',
    ]
    list_filter = [
        'resume',
        'resume__user'
    ]
    fieldsets = (
        (None, {'fields': (
            'resume',
            'first_name', 'last_name', 'about_me',
            'resume_picture', 'date_of_birth', 'nationality',
            'city', 'state', 'country',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )


@admin.register(ContactModel)
class ContactModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = [
        'resume',
        'phone_number', 'email',
    ]
    list_filter = [
        'resume',
        'resume__user'
    ]
    fieldsets = (
        (None, {'fields': (
            'resume',
            'phone_number', 'email', 'address', 'zip_code',
            'facebook', 'linkedin', 'github', 'website',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )


@admin.register(ExperienceModel)
class ExperienceModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = [
        'resume',
        'company_name',
        'position',
        'type',
        'start_date',
        'end_date',
        'is_current',
    ]
    list_filter = [
        'resume',
        'resume__user',
        'type',
        'is_current',
    ]
    fieldsets = (
        (None, {'fields': (
            'resume',
            'company_name', 'position', 'type',
            'start_date', 'end_date', 'is_current',
            'description', 'salary', 'company_website',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )


@admin.register(EducationModel)
class EducationModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = [
        'resume',
        'school_name',
        'degree',
        'department',
        'start_date',
        'end_date',
        'is_current',
    ]
    list_filter = [
        'resume',
        'resume__user',
        'is_current',
    ]
    fieldsets = (
        (None, {'fields': (
            'resume',
            'school_name', 'degree', 'department',
            'grade_scale', 'grade',
            'start_date', 'end_date', 'is_current',
            'description',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )


@admin.register(SkillModel)
class SkillModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = [
        'resume',
        'name',
        'proficiency',
    ]
    list_filter = [
        'resume',
        'resume__user',
        'proficiency',
    ]
    fieldsets = (
        (None, {'fields': (
            'resume',
            'name', 'proficiency',
            'description',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )


@admin.register(LanguageModel)
class LanguageModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = [
        'resume',
        'name',
        'proficiency',
    ]
    list_filter = [
        'resume',
        'resume__user',
        'proficiency',
    ]
    fieldsets = (
        (None, {'fields': (
            'resume',
            'name', 'proficiency',
            'description',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')})
    )


@admin.register(InterestModel)
class InterestModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = [
        'resume',
        'name',
    ]
    list_filter = [
        'resume',
        'resume__user',
    ]
    fieldsets = (
        (None, {'fields': (
            'resume',
            'name',
            'description',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')})
    )


@admin.register(ReferenceModel)
class ReferenceModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = [
        'resume',
        'name',
        'company_name',
        'position',
    ]
    list_filter = [
        'resume',
        'resume__user',
    ]
    fieldsets = (
        (None, {'fields': (
            'resume',
            'name', 'company_name', 'position',
            'phone', 'email',
            'description', 'portfolio',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')})
    )


@admin.register(AwardModel)
class AwardModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = [
        'resume',
        'title',
    ]
    list_filter = [
        'resume',
        'resume__user',
    ]
    fieldsets = (
        (None, {'fields': (
            'resume',
            'title', 'link',
            'description',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')})
    )


@admin.register(CertificationModel)
class CertificationModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = [
        'resume',
        'title',
        'start_date',
    ]
    list_filter = [
        'resume',
        'resume__user',
    ]
    fieldsets = (
        (None, {'fields': (
            'resume',
            'title', 'start_date', 'end_date',
            'description', 'link',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')})
    )

