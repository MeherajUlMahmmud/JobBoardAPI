from django.contrib import admin

from .models import *


class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'job', 'description', 'created_at', 'updated_at')
    list_filter = ('organization', 'job')
    search_fields = ('name', 'description')
    ordering = ('name', 'organization', 'job', 'created_at', 'updated_at')


admin.site.register(ExamModel)
admin.site.register(QuestionModel)
admin.site.register(OptionModel)
admin.site.register(ApplicantResponseModel)
admin.site.register(QuestionResponseModel)
