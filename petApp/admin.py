from django.contrib import admin
from .models import Pet, Appointment, Medication, DietPlan

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'birth_date', 'owner')
    search_fields = ('name', 'species', 'breed')
    list_filter = ('species', 'breed', 'owner')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet', 'veterinarian', 'date')
    search_fields = ('pet_name', 'veterinarian_username')
    list_filter = ('date',)

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('pet', 'name', 'dosage', 'start_date', 'end_date')
    search_fields = ('pet__name', 'name')
    list_filter = ('start_date', 'end_date')

@admin.register(DietPlan)
class DietPlanAdmin(admin.ModelAdmin):
    list_display = ('pet', 'food', 'quantity', 'schedule')
    search_fields = ('pet__name', 'food')
    list_filter = ('schedule',)
# Register your models here.
