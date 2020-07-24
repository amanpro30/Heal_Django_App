from django.forms import ModelForm
from django import forms
from .models import *
# class SlotForm(ModelForm):
#     class Meta:
#         model = Slot
#         fields = ['time_start', 'time_end']
        # widgets = {
        #      'time_start': DatePickerInput(), # default date-format %m/%d/%Y will be used
        #      'time_end': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        #  }

# from pyuploadcare.dj.models import ImageField
class Add_Profile(forms.ModelForm):

    # email_id=forms.CharField(widget=forms.EmailInput)
    dob=forms.DateField(
        widget=forms.DateInput(
        attrs={
        'type':'date',
        }
        )
    )
#     user = forms.CharField(
#     widget=forms.TextInput(attrs={'readonly':'readonly'})
# )
    class Meta:
        model=SampleCollector
        exclude = ('user',)

    def clean_mobile_no(self):
        mobile_no = self.cleaned_data['mobile_no']
        if len(str(mobile_no)) != 10:
            raise forms.ValidationError('enter  a 10 digit number')
        return self.cleaned_data['mobile_no']

class Modify_Profile(forms.ModelForm):
    # email_id=forms.CharField(widget=forms.EmailInput)
    # profile_photo= ImageField(blank=True, manual_crop="")
    class Meta:
        model=SampleCollector
        exclude=('user',)


    def clean_mobile_no(self):
        mobile_no = self.cleaned_data['mobile_no']
        if len(str(mobile_no)) != 10:
            raise forms.ValidationError('enter  a 10 digit number')
        return self.cleaned_data['mobile_no']

