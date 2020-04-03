from django.db import models
from tests.models import Test
# Create your models here.
class Lab(models.Model):
    Male = 'Male'
    Female = 'Female'

    GENDER_CHOICES = (
        (Male, 'Male'),
        (Female, 'Female'),

    )
    
    lab_id=models.CharField(max_length=30,unique=True) 
    name=models.CharField(max_length =100, default='')
    registration=models.CharField(max_length =100, default='')
    owner_name=models.CharField(max_length =100, default='')
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    email_id=models.CharField(max_length=250)
    mobile_no=models.BigIntegerField()
    rating=models.FloatField(default='10.0')

    def __str__(self):
        return self.name

class Lab_Tests(models.Model):
    lab_id=models.ForeignKey(Lab,on_delete=models.CASCADE, null=True,blank=True)        
    test_id=models.ForeignKey(Test,on_delete=models.CASCADE, null=True,blank=True) 