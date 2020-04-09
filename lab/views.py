from django.shortcuts import render

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
