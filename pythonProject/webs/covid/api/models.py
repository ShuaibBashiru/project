from django.db import models

# Create your models here.

class dataSet(models.Model):
    username = models.CharField(max_length=50)
    test_date = models.CharField(max_length=50)
    cough = models.CharField(max_length=50)
    fever = models.CharField(max_length=50)
    sore_throat = models.CharField(max_length=50)
    shortness_of_breath = models.CharField(max_length=50)
    head_ache = models.CharField(max_length=50)
    corona_result = models.CharField(max_length=50)
    age_60_and_above = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    test_indication = models.CharField(max_length=50)
    date_created = models.CharField(max_length=10)
    last_modified = models.CharField(max_length=10)

    class Meta:
        db_table = 'corona_list'
