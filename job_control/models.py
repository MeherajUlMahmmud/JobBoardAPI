from django.db import models

from base.g_models import BaseModel
from user_control.models import ApplicantModel


class JobTypeModel(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Job Types'

    def __str__(self):
        return self.name


class JobModel(BaseModel):
    organization = models.ForeignKey('user_control.OrganizationModel', on_delete=models.CASCADE,
                                     related_name='organization')
    title = models.CharField(max_length=100)
    description = models.TextField()
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_types = models.ManyToManyField(JobTypeModel, related_name='job_types')

    class Meta:
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.title


class JobApplicationModel(BaseModel):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE, related_name='job')
    applicant = models.ForeignKey(ApplicantModel, on_delete=models.CASCADE, related_name='applicant')
    cover_letter = models.TextField()
    status = models.CharField(max_length=100, default='pending')

    class Meta:
        verbose_name_plural = 'Job Applications'

    def __str__(self):
        return self.applicant.user.email
