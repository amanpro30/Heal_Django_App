from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse,reverse_lazy
from .forms import Add_Test

def adminpage(request):
    return render(request, 'adminpage/adminpage.html')

def add_new_test(request):
    if request.method=="POST":
        form=Add_Test(request.POST, request.FILES)

        if form.is_valid():
            test_item=form.save(commit=False)
            test_item.test_id='TEST001'
            test_item.save()

            return redirect('adminpage:adminpage')


    else:

        form=Add_Test()
        #form.fields['user'].widget.attrs['disabled'] = True
        #form.fields['user'].editable=False
    return render(request, 'adminpage/new_test.html', {'form':form})   