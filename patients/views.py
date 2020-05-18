from django.shortcuts import render, redirect
from patients.models import Patient
from django.db.models import Count
    
# Create your views here.
def patient_index(request):
    patients = Patient.objects.all()
    # patients_weekly = Patient.objects.filter(date__month=month).count()
    context = {
        'patients':patients,
        # 'patients_weekly':patients_weekly,
        }
    return render(request, 'patients/patient_lists.html', context)

def patient_detail(request,pk):
    # patient = Patient.objects.get(pk=pk)
    patients = Patient.objects.count()
    context = {
        # 'patient': patient,
        'patients':patients,
        }
    return render(request,'patients/patient_detail.html', context)


def Add_patient(request):
    if request.method =="POST":
        form =request.POST
        #print(form)
        patient= Patient()
        patient.name = form['name']
        patient.mobile = form['mobile']
        patient.id_number = form['id_number']
        patient.address = form['address']
        patient.age = form['age']
        patient.gender = form['gender']
        #patient.address = form['address']
        patient.save()   #insert in database
        
        #give us a new id of the recorded item
        return redirect ('patients:detail', patient.pk)
    return render(request, 'patients/add_patient.html')

