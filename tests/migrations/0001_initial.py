# Generated by Django 3.0.3 on 2020-04-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('condition', models.CharField(choices=[('ALLERGY', 'ALLERGY'), ('ANEMIA', 'AMENIA')], default='', max_length=100)),
                ('test_type', models.CharField(choices=[('BLOOD', 'BLOOD'), ('URINE', 'URINE')], default='', max_length=100)),
                ('pre_test_information', models.CharField(default='', max_length=256)),
                ('description', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]