from django.db import models

from base.g_models import BaseModel
from common.choices import SalaryCurrencyChoices, SalaryPeriodChoices
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
    is_fixed_salary = models.BooleanField(default=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    salary_currency = models.CharField(max_length=100, choices=SalaryCurrencyChoices.choices,
                                       default=SalaryCurrencyChoices.BDT, )
    salary_period = models.CharField(max_length=100, choices=SalaryPeriodChoices.choices,
                                     default=SalaryPeriodChoices.MONTHLY, )
    salary_min = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

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
