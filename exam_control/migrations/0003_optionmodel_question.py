# Generated by Django 4.1.4 on 2023-02-06 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_control', '0002_optionmodel_alter_exammodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='optionmodel',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='option_question', to='exam_control.questionmodel'),
        ),
    ]
