from django.http import HttpResponse, JsonResponse
import json
import random

# Generate 100 medicines with random data
def generate_medicines(n=100):
    bulgarian_medicines = [
        {"title": "Парацетамол", "composition": "Парацетамол", "sideEffects": ["Главоболие", "Гадене", "Сънливост"]},
        {"title": "Аналгин", "composition": "Метамизол натрий", "sideEffects": ["Алергия", "Стомашни болки"]},
        {"title": "Ибупрофен", "composition": "Ибупрофен", "sideEffects": ["Киселини", "Диария"]},
        {"title": "Аспирин", "composition": "Ацетилсалицилова киселина", "sideEffects": ["Кървене", "Стомашен дискомфорт"]},
        {"title": "Амоксицилин", "composition": "Амоксицилин", "sideEffects": ["Обрив", "Диария"]},
        {"title": "Цефуроксим", "composition": "Цефуроксим аксетил", "sideEffects": ["Гадене", "Гъбична инфекция"]},
        {"title": "Кларитромицин", "composition": "Кларитромицин", "sideEffects": ["Безсъние", "Гадене"]},
        {"title": "Диклофенак", "composition": "Диклофенак натрий", "sideEffects": ["Стомашни болки", "Обрив"]},
        {"title": "Лоратадин", "composition": "Лоратадин", "sideEffects": ["Сънливост", "Сухота в устата"]},
        {"title": "Парацетамол + кофеин", "composition": "Парацетамол, кофеин", "sideEffects": ["Безпокойство", "Безсъние"]}
    ]
    medicines = []
    for i in range(n):
        med = bulgarian_medicines[i % len(bulgarian_medicines)].copy()
        med["title"] += f" {i+1}"
        medicines.append(med)
    return medicines

myMedicines = json.dumps(generate_medicines(100))


def home(request): 
    medicines = generate_medicines(100)
    return JsonResponse(medicines, safe=False)

def myMedicines(request): 
    medicines = generate_medicines(100)
    return JsonResponse(medicines, safe=False)


# views.py

from django.http import JsonResponse
from .services.neptune_service import NeptuneService

def medication_prescriptions(request, medication_name="paracetamol"):
    service = NeptuneService()
    prescriptions = service.get_medication_prescriptions(medication_name)
    service.close_connection()
    
    return JsonResponse({'medication': medication_name, 'prescriptions': prescriptions})

def add_medication_view(request):
    medication_name = request.GET.get('name')
    medication_type = request.GET.get('type')
    dosage = request.GET.get('dosage')
    
    service = NeptuneService()
    response = service.add_medication(medication_name, medication_type, dosage)
    service.close_connection()
    
    return JsonResponse({'status': 'success', 'data': response})
