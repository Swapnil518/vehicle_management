from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import VehicleForm
from .models import Vehicle

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicles/vehicle_detail.html', {'vehicle': vehicle})

def vehicle_create(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vehicle_list')
    return render(request, 'vehicles/vehicle_form.html', {'form': form})

def vehicle_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if form.is_valid():
        form.save()
        return redirect('vehicle_list')
    return render(request, 'vehicles/vehicle_form.html', {'form': form})

def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'vehicles/vehicle_confirm_delete.html', {'vehicle': vehicle})


from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'vehicles/register.html', {'form': form})

from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('vehicle_list')
    return render(request, 'vehicles/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def sidebar(request):
    return render(request, 'sidebar.html')

def about_us(request):
    return render(request, 'aboutus.html')
