# Generated by Django 3.0.3 on 2020-04-08 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physiotherapist', '0006_appointmentphysio_slot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmentphysio',
            old_name='Physiotherapist',
            new_name='physiotherapist',
        ),
    ]
