from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime
from django.db.models.signals import pre_save




class Test(models.Model):
    CONDITION_CHOICES=(
        ('ALLERGY', 'ALLERGY'),
        ('ANEMIA', 'AMENIA'),
        
    )
    TEST_TYPE_CHOICES=(
        ('BLOOD', 'BLOOD'),
        ('URINE', 'URINE'),
    )
    
    name=models.CharField(max_length =100, default='',)
    condition=models.CharField(max_length=100, default='', choices=CONDITION_CHOICES)
    test_type=models.CharField(max_length=100, default='', choices=TEST_TYPE_CHOICES)
    price=models.FloatField()
    discounted_price=models.FloatField()
    pre_test_information=models.CharField(max_length=256, default='')
    description=models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.name


