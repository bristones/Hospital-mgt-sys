from django.contrib import admin
from .models import Consultation

# Register your models here.

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'medical_history','admission', 'test_types', 'notes', 'prescription')
    search_fields = ('patient_id', 'medical_history','admission', 'test_types', 'notes', 'prescription')

# allow display on admin page
admin.site.register(Consultation, ConsultationAdmin)
