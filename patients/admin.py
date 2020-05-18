from django.contrib import admin
from .models import Patient

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile','id_number', 'address', 'age', 'gender')
    search_fields = ('name', 'mobile','id_number', 'address', 'age', 'gender')

# allow display on admin page
admin.site.register(Patient, PatientAdmin)

