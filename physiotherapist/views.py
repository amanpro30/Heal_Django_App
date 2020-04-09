from django.shortcuts import render
from .models import Physiotherapist, AppointmentPhysio, Slot
from django.contrib.auth.models import User
from .forms import SlotForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
from django.urls import reverse,reverse_lazy
from django.db.models import Max
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.utils.decorators import method_decorator
from .forms import Add_Profile, Modify_Profile
from django.http import HttpResponseRedirect


def physio_home(request):
    user = request.user
    username = request.user.username
    user_instance = User.objects.get(username=username)
    physio_instance = Physiotherapist.objects.get(user=user_instance)
    upcoming_appointments = AppointmentPhysio.objects.filter(physiotherapist=physio_instance, status='U')
    completed_appointments = AppointmentPhysio.objects.filter(physiotherapist=physio_instance, status='C')
    profile = Physiotherapist.objects.get(user=user)
    if request.method == 'GET':
        slot_form = SlotForm()
    elif request.method == 'POST':
        slot_form = SlotForm(request.POST)
        if slot_form.is_valid():
            slot_instance = slot_form.save(commit=False) 
            date = slot_form.cleaned_data.get('date')
            time_start = slot_form.cleaned_data.get('time_start')
            slot_instance = Slot(date = date, time_start = time_start, physiotherapist=physio_instance)
            slot_instance.save()
    context={
           'profile':profile,
            'upcoming': upcoming_appointments,
            'completed': completed_appointments,
            'slot_form': slot_form,
    }
    
    return render(request, 'physiotherapist/physiotherapist.html',context)

# Create your views here.
def home(request):
    username = request.user.username
    user_instance = User.objects.get(username=username)
    physio_instance = Physiotherapist.objects.get(user=user_instance)
    upcoming_appointments = AppointmentPhysio.objects.filter(physiotherapist=physio_instance, status='U')
    completed_appointments = AppointmentPhysio.objects.filter(physiotherapist=physio_instance, status='C')
    if request.method == 'GET':
        slot_form = SlotForm()
        # slot_form.fields['time_start'].widget = DateTimePickerInput()
    elif request.method == 'POST':
        slot_form = SlotForm(request.POST)
        if slot_form.is_valid():
            slot_form.save()    
    return render(request, 'physiotherapist/physiotherapist1.html',{
        'upcoming': upcoming_appointments,
        'completed': completed_appointments,
        'slot_form': slot_form,
    })

def Booking(request):
    user = request.user
    username = request.user.username
    user_instance = User.objects.get(username=username)
    physio_instance = Physiotherapist.objects.get(user=user_instance)
    upcoming_appointments = AppointmentPhysio.objects.filter(physiotherapist=physio_instance, status='U')
    completed_appointments = AppointmentPhysio.objects.filter(physiotherapist=physio_instance, status='C')
    profile = Physiotherapist.objects.get(user=user)
    if request.method == 'GET':
        slot_form = SlotForm()
    elif request.method == 'POST':
        slot_form = SlotForm(request.POST)
        if slot_form.is_valid():
            slot_instance = slot_form.save(commit=False) 
            date = slot_form.cleaned_data.get('date')
            time_start = slot_form.cleaned_data.get('time_start')
            slot_instance = Slot(date = date, time_start = time_start, physiotherapist=physio_instance)
            slot_instance.save()
    context={
           'profile':profile,
            'upcoming': upcoming_appointments,
            'completed': completed_appointments,
            'slot_form': slot_form,
    }
    
    return render(request, 'physiotherapist/booking.html',context)



def verification(request):
    return render(request,'physiotherapist/verification.html')

def index(request):
     #print(user)

    return render(request,'physiotherapist/profile_home.html')


def make_profile(request):
    user = request.user
    if request.method=="POST":
        form=Add_Profile(request.POST, request.FILES ,initial={'user':user,'email_id':user.email})

        if form.is_valid():
            profile_item=form.save(commit=False)
            profile_item.user = user
            profile_item.verified=False
            profile_item.email_id=user.email
            profile_item.save()

            return render(request, "physiotherapist/verification.html", {})


    else:

        form=Add_Profile(initial={'user':user,'email_id':user.email})
        #form.fields['user'].widget.attrs['disabled'] = True
        #form.fields['user'].editable=False
    return render(request,'new.html',{'form':form})


def modify_profile(request):
    user = request.user
    profile_item = Physiotherapist.objects.get(user=user)
    form=Modify_Profile(request.POST or None, instance=profile_item)
    if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('physiotherapist:physio_home'))
    return render(request,'physiotherapist/new.html',{'form':form})


def Show_Profile(request):
        user = request.user
        profile = Profile.objects.get(user=user)
        context={
            'profile':profile
        }
        if(profile.verified==True):
            print('&&')
            return render(request,'physiotherapist/show_profile.html',context)
        else:
            print('%%')
            return redirect(reverse('doctor_profile:verification'))

def show_slot(request):
    user = request.user
    profile = Physiotherapist.objects.get(user=user)
    context={
        'first_name':profile.first_name,
        'last_name':profile.last_name,
    }
    print(context)

    return render(request,'physiotherapist/show_slot.html',context)


def show_appointments(request):
    user = request.user
    profile = Physiotherapist.objects.get(user=user)
    context={
        'first_name':profile.first_name,
        'last_name':profile.last_name,
    }
    print(context)

    return render(request,'physiotherapist/show_slot.html',context)