from django.contrib import admin
from .models import Pet, GroomingService, Appointment


admin.site.register(Pet)
admin.site.register(GroomingService)
admin.site.register(Appointment)
