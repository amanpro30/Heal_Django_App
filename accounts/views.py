from django.shortcuts import render

# Create your views here.

def home(request):
    context= { "a": "This is a context "}
    return render(request, 'home.html', context=context)


def index(request):
    context= { "a": "This is a context "}
    return render(request, 'account/rmp/login.html', context=context)