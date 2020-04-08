from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    user = request.user
    profile = Physiotherapist.objects.get(user=user)
    context={
           'profile':profile
    }
    
    return render(request, 'physiotherapist/physiotherapist.html',context)