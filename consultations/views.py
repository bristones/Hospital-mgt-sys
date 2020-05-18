from django.shortcuts import render
from django.db.models import Count
from consultations.models import Consultation
from patients.models import Patient

# Create your views here.
def consult(request):
    if request.method =="POST":
        form =request.POST
        consult= Consultation()
        pat_name = Patient()
        pat_name.name = form['patient_id']
        consult.medical_history = form['medical_history']
        consult.admission = form['admission']
        consult.test_types = form['test_types']
        consult.notes = form['notes']
        consult.prescription = form['prescription']
        consult.save()   #insert in database
        
        #give us a new id of the recorded item
        return redirect ('patient:detail', patient.pk)
    return render(request, 'consultations/consult.html')

def Consultation_index(request):
    bed_occupancy = Consultation.objects.filter(admission).count()
    tests = Consultation.objects.filter(test_types)
    pharmacy = Consultation.objects.filter(prescription)
    context = {
        'bed_occupancy':bed_occupancy,
        'tests':tests,
        'prescription':prescription
        }
    return render(request, 'consultations/consult_lists.html', context)