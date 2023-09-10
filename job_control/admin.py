from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from common.admin import RawIdFieldsAdmin
from job_control.models import JobTypeModel, JobModel, JobApplicationModel


@admin.register(JobTypeModel)
class JobTypeAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    fieldsets = (
        (None, {'fields': (
            'name',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )




@admin.register(JobModel)
class JobAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = (
        'title', 'organization',
        'location', 'total_applicants', 'total_views',
    )
    search_fields = ('title', 'organization__name')
    list_filter = ('job_types', 'location')
    readonly_fields = (
        'total_applicants', 'total_views',
    )
    fieldsets = (
        (None, {'fields': (
            'title', 'description', 'organization', 'department', 'location', 'job_types',
            'is_fixed_salary', 'salary', 'salary_currency', 'salary_period', 'salary_min', 'salary_max',
            'total_vacancy',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )


@admin.register(JobApplicationModel)
class JobApplicationAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = (
        'job', 'applicant', 'cover_letter', 'status',
    )
    search_fields = (
        'job__title', 'applicant__user__email',
    )
    list_filter = (
        'status',
    )
    fieldsets = (
        (None, {'fields': (
            'job', 'applicant', 'cover_letter', 'status',
            'extra_fields',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )
