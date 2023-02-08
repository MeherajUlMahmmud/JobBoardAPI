from django.db import models

from base.g_models import BaseModel


class ExamModel(BaseModel):
    organization = models.ForeignKey('user_control.OrganizationModel', on_delete=models.CASCADE)
    job = models.ForeignKey('job_control.JobModel', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    allocated_time = models.IntegerField(default=1)
    total_marks = models.IntegerField(default=0)
    pass_marks = models.IntegerField(default=0)

    class Meta:
        db_table = 'exam'
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'

    def __str__(self):
        return self.name


class QuestionModel(BaseModel):
    QUESTION_TYPE_CHOICES = (
        ('MCQ', 'Multiple Choice Question (MCQ)'),  # Multiple Choice Question (One Answer)
        ('MCQ-M', 'Multiple Choice Question (MCQ-M)'),  # Multiple Choice Question (Multiple Answers)
        # ('FIB', 'Fill in the Blanks (FIB)'),  # Fill in the Blanks
        # ('TF', 'True or False (TF)'),  # True or False
        ('WA', 'Write Answer (WA)'),  # Write Answer
    )
    exam = models.ForeignKey('ExamModel', on_delete=models.CASCADE)
    question = models.TextField()
    type = models.CharField(max_length=255, choices=QUESTION_TYPE_CHOICES, default='MCQ')
    marks = models.IntegerField(default=0)
    options = models.ManyToManyField('OptionModel', related_name='question_options')
    text_answer = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'question'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question


class OptionModel(BaseModel):
    question = models.ForeignKey('QuestionModel', on_delete=models.CASCADE, related_name='option_question', default=None)
    option = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = 'option'
        verbose_name = 'Option'
        verbose_name_plural = 'Options'

    def __str__(self):
        return self.option


class ApplicantResponseModel(BaseModel):
    exam = models.ForeignKey('ExamModel', on_delete=models.CASCADE)
    applicant = models.ForeignKey('user_control.ApplicantModel', on_delete=models.CASCADE)
    total_marks = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True, blank=True)
    submission_time = models.DateTimeField(null=True, blank=True)
    is_submitted = models.BooleanField(default=False)
    is_passed = models.BooleanField(default=False)
    is_late = models.BooleanField(default=False)

    class Meta:
        db_table = 'applicant_response'
        verbose_name = 'Applicant Response'
        verbose_name_plural = 'Applicant Responses'

    def __str__(self):
        return self.exam.name


class QuestionResponseModel(BaseModel):
    applicant_response = models.ForeignKey('ApplicantResponseModel', on_delete=models.CASCADE)
    question = models.ForeignKey('QuestionModel', on_delete=models.CASCADE, related_name='response_question')
    options = models.ManyToManyField('OptionModel', related_name='response_options')
    text_answer = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    obtained_marks = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Question Responses'

    def __str__(self):
        return self.question.question + ' - ' + self.option.option
