from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.db import connection,IntegrityError
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.urls import reverse_lazy
from django import forms

# Create your views here.
def lab_home(request):
	# user = request.user
	# profile = Profile.objects.get(user=user)

	context={

		"premium_content":"Hello u r logged out",
		# "profile":profile
	}
	# if request.user.is_authenticated:
	# 	context["premium_content"]="you are logged in"
	# if(profile.verified==True):
	# 	print('&&')
	return render(request,'lab/lab_homepage.html',context)
	# else:
	# 	print('%%')
	# 	return redirect(reverse('doctor_profile:verification'))

def add_test(request):

	context={

	}	
	return render(request,'lab/lab_add_test.html',context)