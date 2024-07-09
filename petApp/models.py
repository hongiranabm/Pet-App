from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    birth_date = models.DateField()
    medical_history = models.TextField()

class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    veterinarian = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vet_appointments')
    date = models.DateTimeField()
    notes = models.TextField()

class Medication(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    reminder_time = models.TimeField()

class DietPlan(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    food = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    nutrition_notes = models.TextField()
# Create your models here.
