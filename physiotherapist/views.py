from django.shortcuts import render
from .models import Physiotherapist, AppointmentPhysio, Slot
from django.contrib.auth.models import User
from .forms import SlotForm
from bootstrap_datepicker_plus import DateTimePickerInput

# Create your views here.
def home(request):
    username = request.user.username
    user_instance = User.objects.get(username=username)
    physio_instance = Physiotherapist.objects.get(user=user_instance)
    upcoming_appointments = AppointmentPhysio.objects.filter(physiotherapist=physio_instance, status='U')
    completed_appointments = AppointmentPhysio.objects.filter(physiotherapist=physio_instance, status='C')
    if request.method == 'GET':
        slot_form = SlotForm()
        slot_form.fields['time_start'].widget = DateTimePickerInput()
    elif request.method == 'POST':
        slot_form = SlotForm(request.POST)
        if slot_form.is_valid():
            slot_form.save()    
    return render(request, 'physiotherapist/physiotherapist.html',{
        'upcoming': upcoming_appointments,
        'completed': completed_appointments,
        'slot_form': slot_form,
    })