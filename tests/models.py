from django.db import models

# Create your models here.
class Test(models.Model):
    CONDITION_CHOICES=(
        ('ALLERGY', 'ALLERGY'),
        ('ANEMIA', 'AMENIA'),
        
    )
    TEST_TYPE_CHOICES=(
        ('BLOOD', 'BLOOD'),
        ('URINE', 'URINE'),
    )
    test_id=models.CharField(max_length=30,unique=True)
    name=models.CharField(max_length =100, default='')
    condition=models.CharField(max_length=100, default='', choices=CONDITION_CHOICES)
    test_type=models.CharField(max_length=100, default='', choices=TEST_TYPE_CHOICES)
    pre_test_information=models.CharField(max_length=256, default='')
    description=models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.name