from django.db import models

from base.g_models import BaseModel
from common.choices import WorkExperienceTypeChoices, SkillProficiencyLevelChoices, LanguageProficiencyLevelChoices
from user_control.models import UserModel


class ResumeModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='resume')
    name = models.CharField(max_length=255, null=False, blank=False)
    is_education_visible = models.BooleanField(default=True)
    is_experience_visible = models.BooleanField(default=True)
    is_skill_visible = models.BooleanField(default=True)
    is_language_visible = models.BooleanField(default=True)
    is_interest_visible = models.BooleanField(default=True)
    is_reference_visible = models.BooleanField(default=True)
    is_award_visible = models.BooleanField(default=True)
    is_certification_visible = models.BooleanField(default=True)

    class Meta:
        db_table = 'resume'

        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'

    def __str__(self):
        return self.name


class PersonalModel(BaseModel):
    resume = models.OneToOneField(ResumeModel, on_delete=models.CASCADE, related_name='personal')
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    about_me = models.TextField(null=True, blank=True)
    resume_picture = models.ImageField(upload_to='resume_picture/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'personal'

        verbose_name = 'Personal'
        verbose_name_plural = 'Personals'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ContactModel(BaseModel):
    resume = models.OneToOneField(ResumeModel, on_delete=models.CASCADE, related_name='contact')
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'contact'

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    # def __str__(self):
    #     return self.resume


class ExperienceModel(BaseModel):
    resume = models.ForeignKey(ResumeModel, on_delete=models.CASCADE, related_name='experience')
    company_name = models.CharField(max_length=255, null=False, blank=False)
    position = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=255, choices=WorkExperienceTypeChoices.choices,
                            default=WorkExperienceTypeChoices.FULL_TIME)
    start_date = models.DateField(null=False, blank=False)
    is_current = models.BooleanField(default=False)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    company_website = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'experience'

        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.company_name


class EducationModel(BaseModel):
    resume = models.ForeignKey(ResumeModel, on_delete=models.CASCADE, related_name='education')
    school_name = models.CharField(max_length=255, null=False, blank=False)
    degree = models.CharField(max_length=255, null=False, blank=False)
    department = models.CharField(max_length=255, null=False, blank=False)
    grade_scale = models.CharField(max_length=255, null=False, blank=False)
    grade = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'education'

        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        return self.school_name


class SkillModel(BaseModel):
    resume = models.ForeignKey(ResumeModel, on_delete=models.CASCADE, related_name='skill')
    skill = models.CharField(max_length=255, null=False, blank=False)
    proficiency = models.CharField(max_length=255, null=True, blank=True, choices=SkillProficiencyLevelChoices.choices,
                                   default=SkillProficiencyLevelChoices.BEGINNER, )
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'skills'

        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.skill


class LanguageModel(BaseModel):
    resume = models.ForeignKey(ResumeModel, on_delete=models.CASCADE, related_name='language')
    language = models.CharField(max_length=255, null=False, blank=False, default='English')
    proficiency = models.CharField(max_length=255, null=False, blank=False,
                                   choices=LanguageProficiencyLevelChoices.choices,
                                   default=LanguageProficiencyLevelChoices.BASIC, )
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'languages'

        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.language


class InterestModel(BaseModel):
    resume = models.ForeignKey(ResumeModel, on_delete=models.CASCADE, related_name='interest')
    interest = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'interests'

        verbose_name = 'Interest'
        verbose_name_plural = 'Interests'

    def __str__(self):
        return self.interest


class ReferenceModel(BaseModel):
    resume = models.ForeignKey(ResumeModel, on_delete=models.CASCADE, related_name='reference')
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
    resume = models.ForeignKey(ResumeModel, on_delete=models.CASCADE, related_name='award')
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
    resume = models.ForeignKey(ResumeModel, on_delete=models.CASCADE, related_name='certification')
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
