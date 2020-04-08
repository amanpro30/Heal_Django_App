from django.forms import ModelForm
from .models import Slot

class SlotForm(ModelForm):
    class Meta:
        model = Slot
        fields = ('appointment', 'time_start', 'time_end')