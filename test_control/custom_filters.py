from django_filters import CharFilter
from django_filters.rest_framework import FilterSet, DateFromToRangeFilter, BooleanFilter
from django_filters.widgets import BooleanWidget

from common.custom_widgets import CustomTextField, CustomDateRangeFilterWidget, CustomNumberField
from test_control.models import ExamModel, QuestionModel, OptionModel


class ExamModelFilter(FilterSet):
    is_active = BooleanFilter(
        field_name="is_active", label="Is Active",
        widget=BooleanWidget(attrs={'class': 'form-check-input'})
    )
    is_deleted = BooleanFilter(
        field_name="is_deleted", label="Is Deleted",
        widget=BooleanWidget(attrs={'class': 'form-check-input'})
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(attrs={'placeholder': 'YYYY-MM-DD'}),
    )

    class Meta:
        model = ExamModel
        fields = [
            'is_active',
            'is_deleted',
            'created_at',
        ]


class QuestionModelFilter(FilterSet):
    exam = CharFilter(
        field_name="exam", label="Exam ID",
        widget=CustomTextField(attrs={'placeholder': 'Exam ID', 'step': '1'}),
    )
    prompt = CharFilter(
        field_name="prompt", label="Prompt",
        widget=CustomTextField(attrs={'placeholder': 'Prompt'}),
    )
    is_marked = BooleanFilter(
        field_name="is_marked", label="Is Marked",
        widget=BooleanWidget(attrs={'class': 'form-check-input'})
    )
    marks = CharFilter(
        field_name="marks", label="Marks",
        widget=CustomNumberField(attrs={'placeholder': 'Marks', 'step': '1'}),
    )
    is_active = BooleanFilter(
        field_name="is_active", label="Is Active",
        widget=BooleanWidget(attrs={'class': 'form-check-input'})
    )
    is_deleted = BooleanFilter(
        field_name="is_deleted", label="Is Deleted",
        widget=BooleanWidget(attrs={'class': 'form-check-input'})
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(attrs={'placeholder': 'YYYY-MM-DD'}),
    )

    class Meta:
        model = QuestionModel
        fields = [
            'exam',
            'prompt',
            "is_marked",
            "marks",
            'is_active',
            'is_deleted',
            'created_at',
        ]


class OptionModelFilter(FilterSet):
    question = CharFilter(
        field_name="question", label="Question ID",
        widget=CustomTextField(attrs={'placeholder': 'Question ID', 'step': '1'}),
    )
    is_correct = BooleanFilter(
        field_name="is_correct", label="Is Correct",
        widget=BooleanWidget(attrs={'class': 'form-check-input'})
    )
    is_active = BooleanFilter(
        field_name="is_active", label="Is Active",
        widget=BooleanWidget(attrs={'class': 'form-check-input'})
    )
    is_deleted = BooleanFilter(
        field_name="is_deleted", label="Is Deleted",
        widget=BooleanWidget(attrs={'class': 'form-check-input'})
    )
    created_at = DateFromToRangeFilter(
        field_name="created_at", label="Created At",
        widget=CustomDateRangeFilterWidget(attrs={'placeholder': 'YYYY-MM-DD'}),
    )

    class Meta:
        model = OptionModel
        fields = [
            'question',
            'is_correct',
            'is_active',
            'is_deleted',
            'created_at',
        ]
