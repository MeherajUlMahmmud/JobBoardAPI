from rest_framework import serializers

from resume_control.models import *


class ExperienceModelGetSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'company_name', 'position', 'type', 'start_date', 'end_date', 'description')
        depth = 1


class ExperienceModelPostSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'company_name', 'position', 'start_date', 'end_date', 'description')

    def create(self, validated_data):
        experience = ExperienceModel.objects.create(
            user=self.validated_data['user'],
            company_name=self.validated_data['company_name'],
            position=self.validated_data['position'],
            start_date=self.validated_data['start_date'],
            end_date=self.validated_data['end_date'],
            description=self.validated_data['description'] if self.validated_data['description'] else '',
        )
        return experience

    def update(self, instance, validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.position = validated_data.get('position', instance.position)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class EducationModelGetSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'school_name', 'degree', 'department', 'grade', 'start_date', 'end_date', 'description')
        depth = 1


class EducationModelPostSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'school_name', 'degree', 'department', 'grade', 'start_date', 'end_date', 'description')

    def create(self, validated_data):
        education = EducationModel.objects.create(
            user=self.validated_data['user'],
            school_name=self.validated_data['school_name'],
            degree=self.validated_data['degree'],
            department=self.validated_data['department'],
            grade=self.validated_data['grade'],
            start_date=self.validated_data['start_date'],
            end_date=self.validated_data['end_date'],
            description=self.validated_data['description'] if self.validated_data['description'] else '',
        )
        return education

    def update(self, instance, validated_data):
        instance.school_name = validated_data.get('school_name', instance.school_name)
        instance.degree = validated_data.get('degree', instance.degree)
        instance.department = validated_data.get('department', instance.department)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class SkillModelGetSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'skill', 'proficiency', 'description')
        depth = 1


class SkillModelPostSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'skill', 'proficiency', 'description')

    def create(self, validated_data):
        skill = SkillModel.objects.create(
            user=self.validated_data['user'],
            skill=self.validated_data['skill'],
            proficiency=self.validated_data['proficiency'],
            description=self.validated_data['description'] if self.validated_data['description'] else '',
        )
        return skill

    def update(self, instance, validated_data):
        instance.skill = validated_data.get('skill', instance.skill)
        instance.proficiency = validated_data.get('proficiency', instance.proficiency)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class LanguageModelGetSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'language', 'proficiency', 'description')
        depth = 1


class LanguageModelPostSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'language', 'proficiency', 'description')

    def create(self, validated_data):
        language = LanguageModel.objects.create(
            user=self.validated_data['user'],
            language=self.validated_data['language'],
            proficiency=self.validated_data['proficiency'],
            description=self.validated_data['description'] if self.validated_data['description'] else '',
        )
        return language

    def update(self, instance, validated_data):
        instance.language = validated_data.get('language', instance.language)
        instance.proficiency = validated_data.get('proficiency', instance.proficiency)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class InterestModelGetSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'interest', 'description')
        depth = 1


class InterestModelPostSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'interest', 'description')

    def create(self, validated_data):
        interest = InterestModel.objects.create(
            user=self.validated_data['user'],
            interest=self.validated_data['interest'],
            description=self.validated_data['description'] if self.validated_data['description'] else '',
        )
        return interest

    def update(self, instance, validated_data):
        instance.interest = validated_data.get('interest', instance.interest)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class ReferenceModelGetSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'name', 'email', 'phone', 'company_name', 'position', 'description', 'portfolio')
        depth = 1


class ReferenceModelPostSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'name', 'email', 'phone', 'company_name', 'position', 'description' 'portfolio')

    def create(self, validated_data):
        reference = ReferenceModel.objects.create(
            user=self.validated_data['user'],
            name=self.validated_data['name'],
            email=self.validated_data['email'],
            phone=self.validated_data['phone'],
            company_name=self.validated_data['company_name'],
            position=self.validated_data['position'],
            description=self.validated_data['description'] if self.validated_data['description'] else '',
            portfolio=self.validated_data['portfolio'] if self.validated_data['portfolio'] else '',
        )
        return reference

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.position = validated_data.get('position', instance.position)
        instance.description = validated_data.get('description', instance.description)
        instance.portfolio = validated_data.get('portfolio', instance.portfolio)
        instance.save()
        return instance


class AwardModelGetSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'title', 'description', 'link')
        depth = 1


class AwardModelPostSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'title', 'description', 'link')

    def create(self, validated_data):
        award = AwardModel.objects.create(
            user=self.validated_data['user'],
            title=self.validated_data['title'],
            description=self.validated_data['description'] if self.validated_data['description'] else '',
            link=self.validated_data['link'] if self.validated_data['link'] else '',
        )
        return award

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.link = validated_data.get('link', instance.link)
        instance.save()
        return instance


class CertificationModelGetSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'title', 'description', 'link', 'start_date', 'end_date')
        depth = 1


class CertificationModelPostSerializer(serializers.Serializer):
    class Meta:
        fields = ('uuid', 'user', 'title', 'description', 'link', 'start_date', 'end_date')

    def create(self, validated_data):
        certification = CertificationModel.objects.create(
            user=self.validated_data['user'],
            title=self.validated_data['title'],
            description=self.validated_data['description'],
            link=self.validated_data['link'],
            start_date=self.validated_data['start_date'],
            end_date=self.validated_data['end_date'],
        )
        return certification

    def update(self, instance, validated_data):
        instance.certification = validated_data.get('certification', instance.certification)
        instance.description = validated_data.get('description', instance.description)
        instance.link = validated_data.get('link', instance.link)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance
