from django.http import HttpResponse
import json

allMedicines = '[{"title": "парацетамол", "composition":"Парацетамолът се използва като аналгетик и антипиретик. Той е предпочитаната алтернативеа на аспирин, особено при пациенти с нарушения на кръвосъсирването, лица с анамнеза за пептична язва или които не понасят аспирин, както и при деца.", "sideEffects": ["Главоболие", "Гадене", "Опънатост"]}, {"title" : "Аналгин 500мг",  "composition": "Аналгин е обезболяващ лекарствен продукт, който се използва за повлияване на болков синдром от различен произход: зъбобол, невралгии, неврити, миалгии, травми, изгаряния, следперативни болки, фантомна болка, бъбречни и жлъчни колики и главоболие.", "sideEffects": ["Поръщане"]}]'
def home(request): 
    return HttpResponse(allMedicines) 


myMedicines = '[{"title": "парацетамол", "composition":"Парацетамолът се използва като аналгетик и антипиретик. Той е предпочитаната алтернативеа на аспирин, особено при пациенти с нарушения на кръвосъсирването, лица с анамнеза за пептична язва или които не понасят аспирин, както и при деца.", "sideEffects": ["Главоболие", "Гадене", "Опънатост"]}, {"title" : "Аналгин 500мг",  "composition": "Аналгин е обезболяващ лекарствен продукт, който се използва за повлияване на болков синдром от различен произход: зъбобол, невралгии, неврити, миалгии, травми, изгаряния, следперативни болки, фантомна болка, бъбречни и жлъчни колики и главоболие.", "sideEffects": ["Поръщане"]}]'
def myMedicines(request): 
    return HttpResponse(myMedicines) 


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
