from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    context= { "a": "This is a context "}
    return render(request, 'home.html', context=context)


def index(request):
    context= { "a": "This is a context "}
    return render(request, 'account/rmp/login.html', context=context)