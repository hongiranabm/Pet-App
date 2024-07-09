"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from petApp.views import pet_create, pet_list, pet_detail, appointment_list, medication_list, dietplan_list
from django.contrib.auth import views as auth_views
from petApp.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('profile/', profile, name='profile'),
    path('pets/', pet_list, name='pet_list'),
    path('pets/<int:pk>/', pet_detail, name='pet_detail'),
    path('pets/new/', pet_create, name='pet_create'),
    path('appointments/', appointment_list, name='appointment_list'),
    path('medications/', medication_list, name='medication_list'),
    path('dietplans/', dietplan_list, name='dietplan_list'),
]