from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

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

class AppointmentPhysio(models.Model):
    STATUS_CHOICES = (
        ('U', 'Upcoming'),
        ('C', 'Completed'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    physiotherapist = models.ForeignKey(Physiotherapist, on_delete=models.CASCADE)
    def __str__(self):
        return f'Patient:{self.patient}, Physio:{self.physiotherapist}'   

class Slot(models.Model):
    appointment = models.OneToOneField(AppointmentPhysio, on_delete=models.CASCADE)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    def __str__(self):
        return f'{self.appointment}'