from django.db import models

# Create your models here.


class CreateReport(models.Model):
    functions = models.CharField(max_length=200)
    generalPso = models.CharField(max_length=100)
    cognitivePso = models.CharField(max_length=100)
    generalfitness = models.CharField(max_length=100)
    cognitivefitness = models.CharField(max_length=100)
    particle = models.CharField(max_length=100)
    iteration = models.CharField(max_length=100)
    runtime = models.CharField(max_length=100)
    other = models.CharField(max_length=100)
    date_created = models.CharField(max_length=100)

    class Meta:
        db_table = 'report_tbl'
