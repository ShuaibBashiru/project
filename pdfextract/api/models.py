from django.db import models

# Create your models here.

class dataSet(models.Model):
    username = models.CharField(max_length=50)
    areaCode = models.CharField(max_length=50)
    element = models.CharField(max_length=50)
    itemCode = models.CharField(max_length=50)
    item = models.CharField(max_length=50)
    itemYear = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    itemValue = models.CharField(max_length=50)
    date_created = models.CharField(max_length=10)
    last_modified = models.CharField(max_length=10)

    class Meta:
        db_table = 'crop_list'


class Summary_note(models.Model):
    username = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    notetitle = models.CharField(max_length=50)
    summary = models.CharField(max_length=50)
    date_created = models.CharField(max_length=10)
    last_modified = models.CharField(max_length=10)

    class Meta:
        db_table = 'text_summary_tbl'
