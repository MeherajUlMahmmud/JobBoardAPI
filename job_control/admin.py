from django.contrib import admin

from job_control.models import *


class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    ordering = ('created_at',)
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'created_at', 'updated_at')
    ordering = ('created_at',)
    search_fields = ('title', 'organization__name')
    list_filter = ('created_at', 'updated_at')


class JobTypeJobAdmin(admin.ModelAdmin):
    list_display = ('job_type', 'job', 'created_at', 'updated_at')
    ordering = ('created_at',)
    search_fields = ('job_type__name', 'job__title')
    list_filter = ('created_at', 'updated_at')


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'cover_letter', 'status', 'created_at', 'updated_at')
    ordering = ('created_at',)
    search_fields = ('job__title', 'applicant__user__email')
    list_filter = ('status', 'created_at', 'updated_at')


admin.site.register(JobTypeModel, JobTypeAdmin)
admin.site.register(JobModel, JobAdmin)
admin.site.register(JobTypeJobModel, JobTypeJobAdmin)

admin.site.register(JobApplicationModel, JobApplicationAdmin)
