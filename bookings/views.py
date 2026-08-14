from django.shortcuts import render, redirect
from .models import GroomingService
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def services(request):
    services = GroomingService.objects.all()
    return render(request, 'services.html', {'services': services})


@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})
