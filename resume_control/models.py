from django.db import models

from base.g_models import BaseModel
from user_control.models import UserModel


class ExperienceModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, null=False, blank=False)
    position = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'experience'

        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.company_name


class EducationModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255, null=False, blank=False)
    degree = models.CharField(max_length=255, null=False, blank=False)
    department = models.CharField(max_length=255, null=False, blank=False)
    grade = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'education'

        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return self.school_name


class SkillModel(BaseModel):
    SKILL_PROFICIENCY = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Professional', 'Professional'),
    ]
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255, null=False, blank=False)
    proficiency = models.CharField(max_length=255, null=False, blank=False, choices=SKILL_PROFICIENCY)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'skills'

        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.skill


class LanguageModel(BaseModel):
    LANGUAGE_PROFICIENCY = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Professional', 'Professional'),
    ]
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    language = models.CharField(max_length=255, null=False, blank=False)
    proficiency = models.CharField(max_length=255, null=False, blank=False, choices=LANGUAGE_PROFICIENCY)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'languages'

        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.language


class InterestModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    interest = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'interests'

        verbose_name = 'Interest'
        verbose_name_plural = 'Interests'

    def __str__(self):
        return self.interest


class ReferenceModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=255, null=False, blank=False)
    company_name = models.CharField(max_length=255, null=False, blank=False)
    position = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    portfolio = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'references'

        verbose_name = 'Reference'
        verbose_name_plural = 'References'

    def __str__(self):
        return self.name


class AwardModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'awards'

        verbose_name = 'Award'
        verbose_name_plural = 'Awards'

    def __str__(self):
        return self.title


class CertificationModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)

    class Meta:
        db_table = 'certifications'

        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'

    def __str__(self):
        return self.title
