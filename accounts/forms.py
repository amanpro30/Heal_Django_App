from django import forms
from patient.models import Patient
from physiotherapist.models import Physiotherapist
from nurse.models import Nurse
from allauth.account.forms import SignupForm
from django.forms import ModelForm
from django.contrib.auth.models import User

PROFESSION_CHOICES = (
    ('Patient', 'Patient'),
    ('Physiotherapist', 'Physiotherapist'),
    ('Nurse', 'Nurse'),
)

class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(
            required=True, max_length=10)
        self.fields['last_name'] = forms.CharField(
            required=True, max_length=10)
        self.fields['age'] = forms.IntegerField(required=True)
        self.fields['profile_pic'] = forms.ImageField(required=False)
        self.fields['house_no'] = forms.CharField(required=True)
        self.fields['city'] = forms.CharField(required=True)
        self.fields['state'] = forms.CharField(required=True)
        self.fields['pin'] = forms.IntegerField(required=True)
        self.fields['gender'] = forms.CharField(required=True)
        self.fields['dob'] = forms.DateField(required=True, widget=forms.DateInput())
        self.fields['mob_no'] = forms.IntegerField(required=True)
        self.fields['speciality'] = forms.CharField(required=False)
        self.fields['experience'] = forms.IntegerField(required=False)
        self.fields['profession'] = forms.ChoiceField(choices=PROFESSION_CHOICES, widget=forms.RadioSelect())

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        first_name = self.cleaned_data.pop('first_name')
        last_name = self.cleaned_data.pop('last_name')
        age = self.cleaned_data.pop('age')
        profile_pic = self.cleaned_data.pop('profile_pic')
        house_no = self.cleaned_data.pop('house_no')
        city = self.cleaned_data.pop('city')
        state = self.cleaned_data.pop('state')
        pin = self.cleaned_data.pop('pin')
        gender = self.cleaned_data.pop('gender')
        dob = self.cleaned_data.pop('dob')
        mob_no = self.cleaned_data.pop('mob_no')
        speciality = self.cleaned_data.pop('speciality')
        experience = self.cleaned_data.pop('experience')
        profession = self.cleaned_data.pop('profession')
        user_instance = User.objects.get(username=user.username)
        if(profession == 'Patient'):
            patient = Patient(user=user_instance,first_name=first_name,last_name=last_name, age=age,profile_pic=profile_pic,house_no=house_no, city=city, state=state, pin=pin,gender = gender,dob=dob, mob_no = mob_no)
            patient.save()
        elif(profession == 'Physiotherapist'):
            physio = Physiotherapist(user=user_instance,first_name=first_name,last_name=last_name, age=age,profile_pic=profile_pic,house_no=house_no, city=city, state=state, pin=pin,gender = gender,dob=dob, mob_no = mob_no, experience=experience, speciality=speciality)
            physio.save()

        elif(profession == 'Nurse'):
            nurse = Nurse(user=user_instance,first_name=first_name,last_name=last_name, age=age,profile_pic=profile_pic,house_no=house_no, city=city, state=state, pin=pin,gender = gender,dob=dob, mob_no = mob_no,experience = experience, speciality = speciality)
            nurse.save()
        return user
