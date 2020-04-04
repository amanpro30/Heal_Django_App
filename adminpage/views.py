from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse,reverse_lazy


def adminpage(request):
    return render(request, 'adminpage/adminpage.html')

def add_new_test(request):
    return render(request, 'adminpage/new_test.html')   