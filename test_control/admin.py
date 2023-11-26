from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from common.admin import RawIdFieldsAdmin
from test_control.models import ExamModel, QuestionModel, OptionModel


@admin.register(ExamModel)
class ExamModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = (
        'title', 'total_duration', 'total_marks',
    )
    search_fields = ('title',)
    fieldsets = (
        (None, {'fields': (
            'title', 'total_duration', 'total_marks',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )


@admin.register(QuestionModel)
class QuestionModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = ('exam', 'type', 'prompt', 'is_marked', 'marks')
    list_filter = ('exam', 'type', 'is_marked',)
    search_fields = ('prompt',)
    fieldsets = (
        (None, {'fields': (
            'exam', 'type', 'prompt', 'is_marked', 'marks'
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )


@admin.register(OptionModel)
class OptionModelAdmin(ImportExportModelAdmin, RawIdFieldsAdmin):
    list_display = ('question', 'text', 'is_correct')
    list_filter = ('question', 'is_correct',)
    search_fields = ('question__prompt', 'text',)
    fieldsets = (
        (None, {'fields': (
            'question', 'text', 'is_correct',
        )}),
        ('Status', {'fields': ('is_active', 'is_deleted')}),
        ('History', {'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')}),
    )
