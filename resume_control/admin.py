from django.contrib import admin

from resume_control.models import *


class ResumeModelAdmin(admin.ModelAdmin):
    list_display = [
        'uuid',
        'user',
        'name',
        'is_education_visible',
        'is_experience_visible',
        'is_skill_visible',
        'is_language_visible',
        'is_interest_visible',
        'is_reference_visible',
        'is_award_visible',
        'is_certification_visible',
        'created_at',
        'updated_at',
    ]
    list_filter = [
        'user',
    ]
    search_fields = [
        'user',
        'name',
    ]


class PersonalModelAdmin(admin.ModelAdmin):
    list_display = [
        'uuid',
        'resume',
        'first_name',
        'last_name',
    ]


class ContactModelAdmin(admin.ModelAdmin):
    list_display = [
        'uuid',
        'resume',
        'phone_number',
        'email',
        # 'address',
        # 'facebook',
        # 'linkedin',
        # 'github',
    ]


class ExperienceModelAdmin(admin.ModelAdmin):
    list_display = [
        'uuid',
        'resume',
        'company_name',
        'position',
        'type',
        'start_date',
        'end_date',
        'is_current',
        # 'description',
    ]
    list_filter = [
        'resume',
        'resume__user'
    ]

admin.site.register(ResumeModel, ResumeModelAdmin)
admin.site.register(PersonalModel, PersonalModelAdmin)
admin.site.register(ContactModel, ContactModelAdmin)
admin.site.register(ExperienceModel, ExperienceModelAdmin)
admin.site.register(EducationModel)
admin.site.register(SkillModel)
admin.site.register(LanguageModel)
