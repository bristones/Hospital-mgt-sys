from django.conf.urls import url
from django.urls import path
from . import views
from . import models
# from . import PatientsConfig
app_name = 'patients'

urlpatterns = [
    path('add/', views.Add_patient, name='add_patient'),
    path('detail/<int:pk>/', views.patient_detail, name='detail'),
    path('list/', views.patient_index, name='patient_lists'),
]