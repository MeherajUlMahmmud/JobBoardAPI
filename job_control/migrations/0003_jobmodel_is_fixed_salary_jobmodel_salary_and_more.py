# Generated by Django 4.1.4 on 2023-07-03 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_control', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmodel',
            name='is_fixed_salary',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='jobmodel',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='jobmodel',
            name='salary_currency',
            field=models.CharField(choices=[('BDT', 'BDT'), ('USD', 'USD'), ('EUR', 'EUR'), ('INR', 'INR')], default='BDT', max_length=100),
        ),
        migrations.AddField(
            model_name='jobmodel',
            name='salary_max',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='jobmodel',
            name='salary_min',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='jobmodel',
            name='salary_period',
            field=models.CharField(choices=[('hourly', 'Hourly'), ('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], default='monthly', max_length=100),
        ),
    ]