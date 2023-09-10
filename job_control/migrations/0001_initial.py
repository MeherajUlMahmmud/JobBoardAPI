# Generated by Django 4.1.4 on 2023-09-10 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extra_fields', models.JSONField(blank=True, null=True)),
                ('cover_letter', models.TextField()),
                ('status', models.CharField(default='pending', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Job Applications',
            },
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extra_fields', models.JSONField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('department', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('is_fixed_salary', models.BooleanField(default=True)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('salary_currency', models.CharField(choices=[('BDT', 'BDT'), ('USD', 'USD'), ('EUR', 'EUR'), ('INR', 'INR')], default='BDT', max_length=100)),
                ('salary_period', models.CharField(choices=[('hourly', 'Hourly'), ('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], default='monthly', max_length=100)),
                ('salary_min', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('salary_max', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_vacancy', models.IntegerField(default=0)),
                ('total_applicants', models.IntegerField(default=0)),
                ('total_views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='JobTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extra_fields', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Job Types',
            },
        ),
    ]
