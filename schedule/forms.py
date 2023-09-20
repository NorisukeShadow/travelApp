from django import forms
from .models import ScheduleEvent

class ScheduleEventForm(forms.ModelForm):
    class Meta:
        model = ScheduleEvent
        fields = ['title', 'description', 'start_time', 'end_time']
