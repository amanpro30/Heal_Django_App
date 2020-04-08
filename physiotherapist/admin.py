from django.contrib import admin
from .models import Physiotherapist, Slot, AppointmentPhysio

# Register your models here.
admin.site.register(Physiotherapist)
admin.site.register(Slot)
admin.site.register(AppointmentPhysio)