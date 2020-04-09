from django.forms import ModelForm
from django import forms
from .models import Slot
from bootstrap_datepicker_plus import DatePickerInput

class SlotForm(ModelForm):
    class Meta:
        model = Slot
        fields = ['time_start', 'time_end']
        widgets = {
             'time_start': DatePickerInput(), # default date-format %m/%d/%Y will be used
             'time_end': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
         }