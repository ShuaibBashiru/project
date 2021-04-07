from django.db import models

# Create your models here.

class UploadItemModel(models.Model):
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    othername = models.CharField(max_length=50)
    matric = models.CharField(max_length=50)
    levelName = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    courses = models.CharField(max_length=150)
    gpa = models.CharField(max_length=50)
    cgpa = models.CharField(max_length=50)
    program_type = models.CharField(max_length=50)
    date_created = models.CharField(max_length=10)
    last_modified = models.CharField(max_length=10)

    class Meta:
        db_table = 'result_tbl'
