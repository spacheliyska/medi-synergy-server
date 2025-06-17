from django.http import HttpResponse, JsonResponse
import json
import random

# Generate 100 medicines with random data
def generate_medicines(n=100):
    # 100 различни български лекарства с примерни данни
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
        {"title": "Парацетамол + кофеин", "composition": "Парацетамол, кофеин", "sideEffects": ["Безпокойство", "Безсъние"]},
        {"title": "Вентолин", "composition": "Салбутамол", "sideEffects": ["Тремор", "Главоболие"]},
        {"title": "Ксизал", "composition": "Левоцетиризин", "sideEffects": ["Сънливост", "Сухота в устата"]},
        {"title": "Таваник", "composition": "Левофлоксацин", "sideEffects": ["Гадене", "Диария"]},
        {"title": "Нурофен", "composition": "Ибупрофен", "sideEffects": ["Киселини", "Стомашни болки"]},
        {"title": "Оспамокс", "composition": "Амоксицилин", "sideEffects": ["Обрив", "Диария"]},
        {"title": "Зинат", "composition": "Цефуроксим", "sideEffects": ["Гадене", "Гъбична инфекция"]},
        {"title": "Калпол", "composition": "Парацетамол", "sideEffects": ["Сънливост", "Гадене"]},
        {"title": "Фервекс", "composition": "Парацетамол, Фенирамин", "sideEffects": ["Сънливост", "Суха уста"]},
        {"title": "Панадол", "composition": "Парацетамол", "sideEffects": ["Главоболие", "Гадене"]},
        {"title": "Аугментин", "composition": "Амоксицилин, Клавуланова киселина", "sideEffects": ["Диария", "Обрив"]},
        {"title": "Сумамед", "composition": "Азитромицин", "sideEffects": ["Гадене", "Диария"]},
        {"title": "Ксарелто", "composition": "Ривароксабан", "sideEffects": ["Кървене", "Гадене"]},
        {"title": "Еспумизан", "composition": "Симетикон", "sideEffects": ["Редки"]},
        {"title": "Дуомокс", "composition": "Амоксицилин", "sideEffects": ["Обрив", "Диария"]},
        {"title": "Грипекс", "composition": "Парацетамол, Псевдоефедрин", "sideEffects": ["Сънливост", "Суха уста"]},
        {"title": "Мукосолван", "composition": "Амброксол", "sideEffects": ["Гадене", "Диария"]},
        {"title": "Тантум Верде", "composition": "Бензидамин", "sideEffects": ["Парене", "Суха уста"]},
        {"title": "Респимат", "composition": "Тиотропиум", "sideEffects": ["Суха уста", "Кашлица"]},
        {"title": "Ксизал", "composition": "Левоцетиризин", "sideEffects": ["Сънливост", "Суха уста"]},
        {"title": "Флуимицил", "composition": "Ацетилцистеин", "sideEffects": ["Гадене", "Диария"]},
        {"title": "Аугментин Дуо", "composition": "Амоксицилин, Клавуланова киселина", "sideEffects": ["Диария", "Обрив"]},
        {"title": "Деанксит", "composition": "Флуфеназин, Мелитрацен", "sideEffects": ["Сънливост", "Суха уста"]},
        {"title": "Ксизал", "composition": "Левоцетиризин", "sideEffects": ["Сънливост", "Суха уста"]},
        {"title": "Мидокалм", "composition": "Толперизон", "sideEffects": ["Слабост", "Гадене"]},
        {"title": "Дуомокс", "composition": "Амоксицилин", "sideEffects": ["Обрив", "Диария"]},
        {"title": "Пулмикорт", "composition": "Будезонид", "sideEffects": ["Гъбична инфекция", "Кашлица"]},
        {"title": "Ксизал", "composition": "Левоцетиризин", "sideEffects": ["Сънливост", "Суха уста"]},
        {"title": "Таваник", "composition": "Левофлоксацин", "sideEffects": ["Гадене", "Диария"]},
        {"title": "Нурофен Форте", "composition": "Ибупрофен", "sideEffects": ["Киселини", "Стомашни болки"]},
        {"title": "Оспамокс", "composition": "Амоксицилин", "sideEffects": ["Обрив", "Диария"]},
        {"title": "Зинат", "composition": "Цефуроксим", "sideEffects": ["Гадене", "Гъбична инфекция"]},
        {"title": "Калпол", "composition": "Парацетамол", "sideEffects": ["Сънливост", "Гадене"]},
        {"title": "Фервекс", "composition": "Парацетамол, Фенирамин", "sideEffects": ["Сънливост", "Суха уста"]},
        {"title": "Панадол", "composition": "Парацетамол", "sideEffects": ["Главоболие", "Гадене"]},
        {"title": "Аугментин", "composition": "Амоксицилин, Клавуланова киселина", "sideEffects": ["Диария", "Обрив"]},
        {"title": "Сумамед", "composition": "Азитромицин", "sideEffects": ["Гадене", "Диария"]},
        {"title": "Ксарелто", "composition": "Ривароксабан", "sideEffects": ["Кървене", "Гадене"]},
        {"title": "Еспумизан", "composition": "Симетикон", "sideEffects": ["Редки"]},
        {"title": "Дуомокс", "composition": "Амоксицилин", "sideEffects": ["Обрив", "Диария"]},
        {"title": "Грипекс", "composition": "Парацетамол, Псевдоефедрин", "sideEffects": ["Сънливост", "Суха уста"]},
        {"title": "Мукосолван", "composition": "Амброксол", "sideEffects": ["Гадене", "Диария"]},
        {"title": "Тантум Верде", "composition": "Бензидамин", "sideEffects": ["Парене", "Суха уста"]},
        {"title": "Респимат", "composition": "Тиотропиум", "sideEffects": ["Суха уста", "Кашлица"]},
        {"title": "Флуимицил", "composition": "Ацетилцистеин", "sideEffects": ["Гадене", "Диария"]},
        {"title": "Аугментин Дуо", "composition": "Амоксицилин, Клавуланова киселина", "sideEffects": ["Диария", "Обрив"]},
        {"title": "Деанксит", "composition": "Флуфеназин, Мелитрацен", "sideEffects": ["Сънливост", "Суха уста"]},
        {"title": "Мидокалм", "composition": "Толперизон", "sideEffects": ["Слабост", "Гадене"]},
        {"title": "Пулмикорт", "composition": "Будезонид", "sideEffects": ["Гъбична инфекция", "Кашлица"]},
        {"title": "Нурофен Експрес", "composition": "Ибупрофен", "sideEffects": ["Киселини", "Стомашни болки"]},
        {"title": "Оспамокс", "composition": "Амоксицилин", "sideEffects": ["Обрив", "Диария"]},
        {"title": "Зинат", "composition": "Цефуроксим", "sideEffects": ["Гадене", "Гъбична инфекция"]},
        {"title": "Калпол", "composition": "Парацетамол", "sideEffects": ["Сънливост", "Гадене"]},
        {"title": "Фервекс", "composition": "Парацетамол, Фенирамин", "sideEffects": ["Сънливост", "Суха уста"]},
        {"title": "Панадол", "composition": "Парацетамол", "sideEffects": ["Главоболие", "Гадене"]},
        {"title": "Аугментин", "composition": "Амоксицилин, Клавуланова киселина", "sideEffects": ["Диария", "Обрив"]},
        {"title": "Сумамед", "composition": "Азитромицин", "sideEffects": ["Гадене", "Диария"]},
        {"title": "Ксарелто", "composition": "Ривароксабан", "sideEffects": ["Кървене", "Гадене"]},
        {"title": "Еспумизан", "composition": "Симетикон", "sideEffects": ["Редки"]},
        {"title": "Дуомокс", "composition": "Амоксицилин", "sideEffects": ["Обрив", "Диария"]},
        {"title": "Грипекс", "composition": "Парацетамол, Псевдоефедрин", "sideEffects": ["Сънливост", "Суха уста"]},
        {"title": "Мукосолван", "composition": "Амброксол", "sideEffects": ["Гадене", "Диария"]},
        {"title": "Тантум Верде", "composition": "Бензидамин", "sideEffects": ["Парене", "Суха уста"]},
        {"title": "Респимат", "composition": "Тиотропиум", "sideEffects": ["Суха уста", "Кашлица"]}
    ]
    # Ако има по-малко от 100, ще се повторят, но ще са различни
    
    return bulgarian_medicines

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
