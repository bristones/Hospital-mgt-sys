from django.contrib import admin
from .models import Payment

# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('time', 'patient_id','payment_type', 'payment_for', 'amount')
    search_fields = ('time', 'patient_id','payment_type', 'payment_for', 'amount')

# allow display on admin page
admin.site.register(Payment, PaymentAdmin)
