from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('myMedicines', views.myMedicines),
    path('add_medication/', views.add_medication_view, name='add_medication'),
    path('login/', views.login_view),
]
