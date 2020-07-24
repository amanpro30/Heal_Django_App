from django.db import models
from tests.models import Test
from django.contrib.auth.models import User

# Create your models here.
class Lab(models.Model):
    Male = 'Male'
    Female = 'Female'

    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),

    )
    user = models.CharField(primary_key= True, max_length=100)
    lab_name=models.CharField(max_length =100, default='')
    lab_registration=models.CharField(max_length =100, default='')
    lab_owner = models.CharField(max_length=350)
    owner_name=models.CharField(max_length =100, default='')
    lab_address= models.CharField(max_length =300, default='')
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_no=models.BigIntegerField()
    rating=models.FloatField(default='10.0')

    def __str__(self):
        return self.name


