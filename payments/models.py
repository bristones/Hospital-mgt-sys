from django.db import models
from patients.models import Patient
from django.utils import timezone

# Create your models here.
class Payment(models.Model):
    time = models.DateTimeField(default=timezone.now)
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE,default=1)
    PAYMENT_TYPES = (
        ('Cash', 'Cash'),
        ('Mpesa', 'Mobile_money'),
        ('Insurance', 'Insurance'),
        ('Card', 'Card'),
    )
    payment_type = models.CharField(max_length=9, choices=PAYMENT_TYPES)
    PAYMENT_FOR_OPTIONS = (
        ('Lab', 'Labaratory'),
        ('Con', 'Consultations'), #to include diagnosis and ather specialized services like dental etc
        ('Pharm', 'Pharmacy'),
        ('Ward', 'Admisions'),
        ('All', 'All payments'),
    )
    payment_for = models.CharField(max_length=15, choices=PAYMENT_FOR_OPTIONS)
    amount = models.IntegerField()
    
    
    class Meta:
        db_table = 'payments'
        managed = True #flush or sync db
    
    def __str__(self):
        return self.amount


# patient id, past history, history, test-types, notes, prescriptions