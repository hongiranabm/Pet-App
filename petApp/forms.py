from django import forms
from .models import Pet, Appointment, Medication, DietPlan

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'birth_date', 'medical_history']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['pet', 'veterinarian', 'date', 'notes']

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['pet', 'name', 'dosage', 'start_date', 'end_date', 'reminder_time']

class DietPlanForm(forms.ModelForm):
    class Meta:
        model = DietPlan
        fields = ['pet', 'food', 'quantity', 'schedule', 'nutrition_notes']