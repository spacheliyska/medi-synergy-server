from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('myMedicines', views.medication_prescriptions),
    path('add_medication/', views.add_medication_view, name='add_medication'),
]
