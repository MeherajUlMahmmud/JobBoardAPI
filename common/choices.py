from django.db import models


class SalaryPeriodChoices(models.TextChoices):
    HOURLY = "hourly", "Hourly"
    DAILY = "daily", "Daily"
    WEEKLY = "weekly", "Weekly"
    MONTHLY = "monthly", "Monthly"
    YEARLY = "yearly", "Yearly"


class SalaryCurrencyChoices(models.TextChoices):
    BDT = "BDT", "BDT"
    USD = "USD", "USD"
    EUR = "EUR", "EUR"
    INR = "INR", "INR"


class LanguageProficiencyLevelChoices(models.TextChoices):
    BASIC = "Basic", "Basic"
    CONVERSATIONAL = "Conversational", "Conversational"
    FLUENT = "Fluent", "Fluent"
    NATIVE = "Native", "Native"


class SkillProficiencyLevelChoices(models.TextChoices):
    BEGINNER = "Beginner", "Beginner"
    INTERMEDIATE = "Intermediate", "Intermediate"
    ADVANCED = "Advanced", "Advanced"
    EXPERT = "Expert", "Expert"


class WorkExperienceTypeChoices(models.TextChoices):
    FULL_TIME = "Full Time", "Full Time"
    PART_TIME = "Part Time", "Part Time"
    INTERNSHIP = "Internship", "Internship"
    CONTRACT = "Contract", "Contract"
    FREELANCE = "Freelance", "Freelance"
    VOLUNTEER = "Volunteer", "Volunteer"
    APPRENTICESHIP = "Apprenticeship", "Apprenticeship"
    TRAINEESHIP = "Traineeship", "Traineeship"
