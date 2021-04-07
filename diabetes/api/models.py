from django.db import models

# Create your models here.

class dataSet(models.Model):
    username = models.CharField(max_length=50)
    glucose = models.CharField(max_length=50)
    bloodPressure = models.CharField(max_length=50)
    skinThickness = models.CharField(max_length=50)
    insulin = models.CharField(max_length=50)
    bmi = models.CharField(max_length=50)
    pedigreeFunction = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    outcome = models.CharField(max_length=50)
    date_created = models.CharField(max_length=10)
    last_modified = models.CharField(max_length=10)

    class Meta:
        db_table = 'diabetes_list'
