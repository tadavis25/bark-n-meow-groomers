from django import forms
from .models import Appointment, Pet
from django.utils import timezone


class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['pet'].queryset = Pet.objects.filter(owner=user)

    class Meta:
        model = Appointment
        fields = ['pet', 'service', 'appointment_date', 
                  'appointment_time', 'notes', ]

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
        ]
