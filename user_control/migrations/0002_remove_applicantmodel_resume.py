# Generated by Django 4.1.4 on 2023-11-27 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_control', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicantmodel',
            name='resume',
        ),
    ]