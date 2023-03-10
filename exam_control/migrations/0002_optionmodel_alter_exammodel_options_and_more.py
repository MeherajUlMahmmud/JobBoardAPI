# Generated by Django 4.1.4 on 2023-01-17 10:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0001_initial'),
        ('exam_control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('option', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
                'db_table': 'option',
            },
        ),
        migrations.AlterModelOptions(
            name='exammodel',
            options={'verbose_name': 'Exam', 'verbose_name_plural': 'Exams'},
        ),
        migrations.AddField(
            model_name='exammodel',
            name='allocated_time',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='exammodel',
            name='pass_marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exammodel',
            name='total_marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='exammodel',
            table='exam',
        ),
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.TextField()),
                ('type', models.CharField(choices=[('MCQ', 'Multiple Choice Question (MCQ)'), ('MCQ-M', 'Multiple Choice Question (MCQ-M)')], default='MCQ', max_length=255)),
                ('marks', models.IntegerField(default=0)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_control.exammodel')),
                ('options', models.ManyToManyField(related_name='question_options', to='exam_control.optionmodel')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='ApplicantResponseModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_marks', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('submission_time', models.DateTimeField(blank=True, null=True)),
                ('is_submitted', models.BooleanField(default=False)),
                ('is_passed', models.BooleanField(default=False)),
                ('is_late', models.BooleanField(default=False)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_control.applicantmodel')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_control.exammodel')),
            ],
            options={
                'verbose_name': 'Applicant Response',
                'verbose_name_plural': 'Applicant Responses',
                'db_table': 'applicant_response',
            },
        ),
        migrations.CreateModel(
            name='QuestionResponseModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('obtained_marks', models.IntegerField()),
                ('answer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='response_answer', to='exam_control.optionmodel')),
                ('applicant_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_control.applicantresponsemodel')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response_option', to='exam_control.optionmodel')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response_question', to='exam_control.questionmodel')),
            ],
            options={
                'verbose_name_plural': 'Question Responses',
                'unique_together': {('applicant_response', 'answer')},
            },
        ),
    ]
