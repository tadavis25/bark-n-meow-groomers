from django import forms
from .models import Appointment, Pet


class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if user:
            self.fields['pet'].queryset = Pet.objects.filter(owner=user)

    class Meta:
        model = Appointment
        fields = ['pet', 'service', 'appointment_date', 
                  'appointment_time', 'notes', ]


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
