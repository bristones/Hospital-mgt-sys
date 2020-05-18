from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.daraja.mpesa.core import MpesaClient
from django.urls import reverse
from payments.models import Payment
from patients.models import Patient


# Create your views here.
def Payment_index(request):
    cl = MpesaClient()
    token = cl.access_token
    print(token)
    #use a safaricom phone number you can access
    phone_number = '0727618922'
    amount = 2
    account_reference
    transaction_desc
    callback_url
    response 
    return HttpResponse(response, text)
    # if request.method =="POST":
    #     form =request.POST
    #     #print(form)
    #     payment= Payment()
    #     payment.name = form['time']
    #     payment.mobile = form['patient_id']
    #     payment.id_number = form['payment_type']
    #     payment.address = form['payment_for']
    #     payment.age = form['amount']
        
def stk_push_callback(request):
    data = request.body
    json _data = json.loads(data)
    print(json_data)
    print(json_data['partyB'])
    
    return HttpResponse(data)

    return render(request, 'payments/make_payment.html', context)


        
def Payment_Report(request): 

    patients = Patient.objects.all()

     
    context ={
        'patients':patients,
    }
    return render(request, "payments/payment_history.html",context)
    
