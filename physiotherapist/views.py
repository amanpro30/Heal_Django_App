from django.shortcuts import render
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
    profile_item = Profile.objects.get(user=user)
    form=Modify_Profile(request.POST or None, instance=profile_item)
    if form.is_valid():
            form.save()
            return redirect('/doctor_home/')
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




