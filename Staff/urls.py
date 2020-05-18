from django.conf.urls import url
from django.urls import path
from . import views
from . import models

app_name = 'staff'

urlpatterns = [
    path('', views.UserLogin, name='login'),
    path('dashboard/', views.staffProfile, name='profile'),
    path('account_registration/', views.Register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]