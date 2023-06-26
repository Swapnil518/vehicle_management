from django import forms
from .models import Vehicle
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
