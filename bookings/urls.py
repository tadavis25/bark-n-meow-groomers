from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('add-pet/', views.add_pet, name='add_pet'),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
    path('cancel-appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('signup/', views.signup, name='signup'),
    path('my-pets/', views.my_pets, name='my_pets'),
    path('edit-pet/<int:pet_id>/', views.edit_pet, name='edit_pet'),
    path('delete-pet/<int:pet_id>/', views.delete_pet, name='delete_pet'),

]
