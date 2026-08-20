from django.shortcuts import render, redirect, get_object_or_404
from .models import GroomingService, Appointment, Pet
from .forms import AppointmentForm, PetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


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
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        user=request.user
    )

    if request.method == "POST":
        form = AppointmentForm(
            request.POST,
            instance=appointment,
            user=request.user
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Appointment updated successfully!"
            )
            return redirect("my_appointments")
    else:
        form = AppointmentForm(
            instance=appointment,
            user=request.user
        )

    return render(
        request,
        "edit_appointment.html",
        {"form": form, "appointment": appointment}
    )


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
        messages.success(request, "Appointment cancelled successfully!")

    return redirect('my_appointments')


@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, user=request.user)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            messages.success(request, "Appointment booked successfully!")
            return redirect('home')
    else:
        form = AppointmentForm(user=request.user)
    return render(request, 'book_appointment.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully!")
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


@login_required
def add_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)

        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect("book_appointment")
    else:
        form = PetForm()

    return render(request, "add_pet.html", {"form": form})

@login_required
def my_pets(request):
    pets = Pet.objects.filter(owner=request.user)
    return render(request, "my_pets.html", {"pets": pets})


@login_required
def edit_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)

    if request.method == "POST":
        form = PetForm(request.POST, request.FILES, instance=pet)

        if form.is_valid():
            form.save()
            messages.success(request, "Pet details updated successfully!")
            return redirect("my_pets")
    else:
        form = PetForm(instance=pet)

    return render(request, "edit_pet.html", {"form": form, "pet": pet})

@login_required
def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)

    if request.method == "POST":
        pet.delete()
        messages.success(request, "Pet deleted successfully!")
        return redirect("my_pets")

    return render(request, "delete_pet.html", {"pet": pet})
