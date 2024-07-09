from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import Pet, Appointment, Medication, DietPlan
from django.contrib.auth.forms import UserCreationForm
from django.template import loader
from petApp.forms import PetForm, AppointmentForm, MedicationForm, DietPlanForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def pet_list(request):
    pets = Pet.objects.filter(owner=request.user)
    return render(request, 'pet_list.html', {'pets': pets})

def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})

def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'pet_form.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.filter(pet__owner=request.user)
    return render(request, 'appointment_list.html', {'appointments': appointments})

def medication_list(request):
    medications = Medication.objects.filter(pet__owner=request.user)
    return render(request, 'medication_list.html', {'medications': medications})

def dietplan_list(request):
    dietplans = DietPlan.objects.filter(pet__owner=request.user)
    return render(request, 'dietplan_list.html', {'dietplans': dietplans})

def gettime1(request):
    return HttpResponse('welcome to lab')
# Create your views here.
