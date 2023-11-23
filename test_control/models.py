from django.db import models

from common.choices import QuestionTypeChoices
from common.models import BaseModel


class ExamModel(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    total_duration = models.IntegerField(default=0)
    total_marks = models.FloatField(default=0)

    class Meta:
        db_table = 'exams'
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class QuestionModel(BaseModel):
    exam = models.ForeignKey(ExamModel, on_delete=models.RESTRICT, related_name='questions')
    type = models.CharField(max_length=4, choices=QuestionTypeChoices.choices, default=QuestionTypeChoices.MCQ)
    prompt = models.TextField(null=True, blank=True)
    is_marked = models.BooleanField(default=True)
    marks = models.FloatField(default=1)

    class Meta:
        db_table = 'questions'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        ordering = ['id']

    def __str__(self):
        return self.exam.title + ' - ' + self.prompt


class OptionModel(BaseModel):
    question = models.ForeignKey(QuestionModel, on_delete=models.RESTRICT, related_name='options')
    text = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = 'options'
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
        ordering = ['id']

    def __str__(self):
        return self.question.exam.title + ' - ' + self.question.prompt
