# Generated by Django 3.0.3 on 2020-04-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20200405_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='discounted_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='test',
            name='price',
            field=models.FloatField(),
        ),
    ]
