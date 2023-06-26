from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('vehicle_list', v.vehicle_list, name='vehicle_list'),
    path('vehicle/create/', v.vehicle_create, name='vehicle_create'),
    path('vehicle/<int:pk>/', v.vehicle_detail, name='vehicle_detail'),
    path('vehicle/<int:pk>/update/', v.vehicle_update, name='vehicle_update'),
    path('vehicle/<int:pk>/delete/', v.vehicle_delete, name='vehicle_delete'),
    path('vehicle/sidebar', v.sidebar, name='sidebar'),
]
