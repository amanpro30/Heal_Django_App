# Generated by Django 3.0.3 on 2020-07-24 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleCollector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('bike_available', models.BooleanField(default=True)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('profile_pic', models.ImageField(blank=True, default='patient.png', null=True, upload_to='SampleCollector')),
                ('house_no', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pin', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Undisclosed')], max_length=1)),
                ('dob', models.DateField()),
                ('mob_no', models.BigIntegerField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
