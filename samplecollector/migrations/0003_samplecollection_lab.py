# Generated by Django 3.0.3 on 2020-07-19 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab1', '0001_initial'),
        ('samplecollector', '0002_samplecollection'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplecollection',
            name='lab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab1.Lab1'),
        ),
    ]
