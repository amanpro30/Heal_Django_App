from django.db import models

# Create your models here.
class Host(models.Model):
    name=models.CharField(max_length =100, default='')
    email_address=models.EmailField(max_length = 254) 
    phone=models.BigIntegerField()
    address=models.CharField(max_length=100,default='', blank=True)

    def __str__(self):
        return self.name