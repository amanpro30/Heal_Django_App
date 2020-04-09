# Generated by Django 3.0.3 on 2020-04-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurse',
            name='email',
        ),
        migrations.RemoveField(
            model_name='nurse',
            name='is_verified',
        ),
        migrations.AlterField(
            model_name='nurse',
            name='profile_pic',
            field=models.ImageField(blank=True, default='nurse.jpeg', upload_to='Nurse_pics'),
        ),
    ]
