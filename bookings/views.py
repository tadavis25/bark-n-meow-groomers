from django.shortcuts import render, redirect, get_object_or_404
from .models import GroomingService, Appointment
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def home(request):
    return render(request, 'home.html')


def services(request):
    services = GroomingService.objects.all()
    return render(request, 'services.html', {'services': services})


@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user).exclude(status='cancelled')
    return render(request, 'my_appointments.html', {'appointments': appointments})


@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        user=request.user
    )

    if request.method == 'POST':
        appointment.status = 'cancelled'
        appointment.save()

    return redirect('my_appointments')


@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, user=request.user)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('home')
    else:
        form = AppointmentForm(user=request.user)
    return render(request, 'book_appointment.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})
