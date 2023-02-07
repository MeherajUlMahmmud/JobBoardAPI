from django.contrib import admin

from .models import *


class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'job', 'description', 'created_at', 'updated_at')
    list_filter = ('organization', 'job')
    search_fields = ('name', 'description')
    ordering = ('name', 'organization', 'job', 'created_at', 'updated_at')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'exam', 'created_at', 'updated_at')
    list_filter = ('exam',)
    search_fields = ('question',)
    ordering = ('exam', 'created_at', 'updated_at')


class OptionAdmin(admin.ModelAdmin):
    list_display = ('option', 'question', 'is_correct', 'created_at', 'updated_at')
    list_filter = ('question',)
    search_fields = ('option',)
    ordering = ('question', 'created_at', 'updated_at')


admin.site.register(ExamModel, ExamAdmin)
admin.site.register(QuestionModel, QuestionAdmin)
admin.site.register(OptionModel, OptionAdmin)
admin.site.register(ApplicantResponseModel)
admin.site.register(QuestionResponseModel)
