from django.conf.urls import url
from django.urls import path
from . import views
from . import models

app_name = 'payments'

urlpatterns = [
    path('pay/', views.Payment_index, name='make_payment'),
    path('payment_history/', views.Payment_Report, name='payment_list'),
]