from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['pet', 'service', 'appointment_date', 
                  'appointment_time', 'notes', ]
