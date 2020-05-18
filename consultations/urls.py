from django.conf.urls import url
from django.urls import path
from . import views
from . import models

app_name = 'consultations'

urlpatterns = [
    path('make_consultation', views.consult, name='consult'),
    path('consultation_lists', views.Consultation_index, name='consult_lists'),
]