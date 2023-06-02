from django.db import models


class WorkExperienceTypeChoices(models.TextChoices):
    FULL_TIME = "Full Time", "Full Time"
    PART_TIME = "Part Time", "Part Time"
    INTERNSHIP = "Internship", "Internship"
    CONTRACT = "Contract", "Contract"
    FREELANCE = "Freelance", "Freelance"
    VOLUNTEER = "Volunteer", "Volunteer"
    APPRENTICESHIP = "Apprenticeship", "Apprenticeship"
    TRAINEESHIP = "Traineeship", "Traineeship"
