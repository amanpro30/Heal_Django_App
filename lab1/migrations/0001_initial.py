# Generated by Django 3.0.3 on 2020-07-24 05:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('samplecollector', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.CharField(default='', max_length=100)),
                ('lab_registration', models.CharField(default='', max_length=100)),
                ('lab_owner', models.CharField(max_length=350)),
                ('lab_address', models.CharField(default='', max_length=300)),
                ('mobile_no', models.BigIntegerField()),
                ('profile_photo', models.ImageField(upload_to='media_/physio_profile_pic/')),
                ('house_no', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pin', models.IntegerField()),
                ('rating', models.FloatField(default=0.0)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LabSlot1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Test1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('condition', models.CharField(choices=[('ALLERGY', 'ALLERGY'), ('ANEMIA', 'AMENIA')], default='', max_length=100)),
                ('test_type', models.CharField(choices=[('BLOOD', 'BLOOD'), ('URINE', 'URINE')], default='', max_length=100)),
                ('price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('pre_test_information', models.CharField(default='', max_length=256)),
                ('description', models.CharField(default='', max_length=1000)),
                ('photo', models.ImageField(null=True, upload_to='media_/lab_pics/')),
                ('collector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='samplecollector.SampleCollector')),
            ],
        ),
        migrations.CreateModel(
            name='Lab_complaint_feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specify_type', models.CharField(choices=[('SALARY', 'SALARY'), ('BOOKING', 'BOOKING'), ('OTHER/FEEDBACK', 'OTHER/FEEDBACK')], max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('SENT TO ADMIN', 'SENT TO ADMIN'), ('RESOLVED', 'RESOLVED')], default='SENT TO ADMIN', max_length=200)),
                ('description', models.TextField()),
                ('lab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab1.Lab1')),
            ],
        ),
        migrations.CreateModel(
            name='BookingDateLab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('lab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab1.Lab1')),
            ],
        ),
        migrations.CreateModel(
            name='SampleCollectionSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(blank=True, choices=[('09:00:00', '9 am'), ('10:00:00', '10 am'), ('11:00:00', '11 am'), ('12:00:00', '12 pm'), ('13:00:00', '1 pm'), ('14:00:00', '2 pm'), ('15:00:00', '3 pm'), ('16:00:00', '4 pm'), ('17:00:00', '5 pm'), ('18:00:00', '6 pm')], max_length=200, null=True)),
                ('slot_status', models.BooleanField(default=False)),
                ('date', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab1.BookingDateLab')),
                ('lab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab1.Lab1')),
            ],
            options={
                'unique_together': {('lab', 'start_time', 'date')},
            },
        ),
    ]