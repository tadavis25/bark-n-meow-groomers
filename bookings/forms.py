from django import forms
from .models import Appointment, Pet
from django.utils import timezone


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['pet'].queryset = Pet.objects.filter(owner=user)

        self.fields['appointment_date'].widget = DateInput()
        self.fields['appointment_time'].widget = TimeInput(
              attrs={'step': 900})

    class Meta:
        model = Appointment
        fields = ['pet', 'service', 'appointment_date', 
                  'appointment_time', 'notes', ]

    widgets = {
        'appointment_date': DateInput(),
    }

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data["appointment_date"]

        if appointment_date < timezone.localdate():
            raise forms.ValidationError("Appointment date cannot be in the past.")

        return appointment_date


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'name',
            'age',
            'pet_type',
            'size',
            'breed',
            'notes',
            'image',
        ]
