from django.db import models

# Create your models here.
class Nurse(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Undisclosed'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    speciality = models.CharField(max_length=20)
    experience = models.IntegerField()
    profile_pic = models.ImageField()
    house_no = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.IntegerField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    dob = models.DateField()
    mob_no = models.IntegerField()
    email = models.EmailField()
    rating = models.FloatField()
    is_verified = models.BooleanField()

    def __str__(self):
        return f'{self.first_name}'