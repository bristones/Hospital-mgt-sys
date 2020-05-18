from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    id_number = models.CharField(max_length=10,unique=True)
    address = models.CharField(max_length=10)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    
    class Meta:
        db_table = 'patients'
        managed = True #flush or sync db
    
    def __str__(self):
        return self.name 
