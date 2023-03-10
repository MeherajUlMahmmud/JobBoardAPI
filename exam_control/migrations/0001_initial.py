# Generated by Django 4.1.4 on 2023-01-17 10:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_control', '0001_initial'),
        ('job_control', '0003_alter_jobapplicationmodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_control.jobmodel')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_control.organizationmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
