from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Pet(models.Model):
    PET_TYPES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
    ]

    PET_SIZES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=10, choices=PET_TYPES)
    breed = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField()
    size = models.CharField(max_length=10, choices=PET_SIZES)
    notes = models.TextField(blank=True)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name


class GroomingService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    service = models.ForeignKey(GroomingService, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pet.name} - {self.appointment_date}"
