# Generated by Django 4.1.4 on 2024-03-17 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_control', '0003_awardmodel_serial_certificationmodel_serial_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalmodel',
            name='resume_picture',
            field=models.TextField(blank=True, null=True),
        ),
    ]
