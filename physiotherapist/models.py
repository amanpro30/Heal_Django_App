from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
from datetime import datetime

# Create your models here.
class Physiotherapist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    profile_pic = models.ImageField(default='physio.jpeg', upload_to='Physio_pics', blank=True)
    house_no = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.IntegerField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    dob = models.DateField()
    mob_no = models.BigIntegerField()
    rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return f'{self.first_name}'

class Slot(models.Model):
    date = models.DateField(default=datetime.now)
    physiotherapist = models.ForeignKey(Physiotherapist, on_delete=models.CASCADE)
    TIME_CHOICES = (
        ('09:00:00', '9 am'),
                    ('10:00:00', '10 am'),
                    ('11:00:00', '11 am'),
                    ('12:00:00', '12 am'),
                    ('13:00:00', '1 pm'),
                    ('14:00:00', '2 pm'),
                    ('15:00:00', '3 pm'),
                    ('16:00:00', '4 pm'),
                    ('17:00:00', '5 pm'),
                    ('18:00:00', '6 pm'),
                    )
    time_start = models.CharField(max_length=200,choices=TIME_CHOICES,null=True,blank=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.time_start}'

class AppointmentPhysio(models.Model):
    STATUS_CHOICES = (
        ('U', 'Upcoming'),
        ('C', 'Completed'),
    )
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    physiotherapist = models.ForeignKey(Physiotherapist, on_delete=models.CASCADE)
    def __str__(self):
        return f'Patient:{self.patient}, Physio:{self.physiotherapist}'   
