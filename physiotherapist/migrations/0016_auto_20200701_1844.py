# Generated by Django 3.0.3 on 2020-07-01 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('physiotherapist', '0015_auto_20200701_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='physiotherapist_complaint_feedback',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='physiotherapist_complaint_feedback',
            name='status',
            field=models.CharField(choices=[('SENT TO ADMIN', 'SENT TO ADMIN'), ('RESOLVED', 'RESOLVED')], default='SENT TO ADMIN', max_length=200),
        ),
    ]