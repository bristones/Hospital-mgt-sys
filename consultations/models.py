from django.db import models
from patients.models import Patient

# Create your models here.   # patient id, past history, history, test-types, notes, prescriptions
class Consultation(models.Model):
    patient_id = models.ForeignKey(Patient,on_delete=models.CASCADE,default=1)
    medical_history = models.CharField(max_length=100)
    ADMISSION_TYPES = (
        ('Y', 'Yes'),   
        ('N', 'No'),
    )
    admission = models.CharField(max_length=5, choices=ADMISSION_TYPES)
    TEST_TYPES = (
        ('Lab', 'Labaratory'),   
        ('cardio', 'cardiovascular'),
        ('skin', 'dermatology'),
        ('ENT', 'ENT'),
        ('gastro', 'gastrointerstinal'),
        ('blood', 'haematology'),
        ('brain', 'neurological'),
        ('gynae', 'gynaelogical'),
        ('visual', 'ocular'),
        ('joints', 'rheumatology'),
        ('heart', 'pulmonary'),
        ('imaging', 'radiology'),
        ('urine', 'urology'),
    )
    test_types = models.CharField(max_length=20, choices=TEST_TYPES )
    notes = models.CharField(max_length=500)
    prescription = models.CharField(max_length=300)
    

    class Meta:
        db_table = 'consultations'
        managed = True #flush or sync db
    
    def __str__(self):
        return self.test_types


