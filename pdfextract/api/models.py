from django.db import models

# Create your models here.

class fileUpload(models.Model):

    user_id = models.CharField(max_length=50)
    file_title = models.CharField(max_length=50)
    file_name = models.CharField(max_length=50)
    date_created = models.CharField(max_length=10)
    last_modified = models.CharField(max_length=10)

    class Meta:
        db_table = 'file_uploads_tbl'


class Summary_note(models.Model):
    username = models.CharField(max_length=50)
    notes = models.CharField(max_length=50)
    notetitle = models.CharField(max_length=50)
    summary = models.CharField(max_length=50)
    date_created = models.CharField(max_length=10)
    last_modified = models.CharField(max_length=10)

    class Meta:
        db_table = 'text_summary_tbl'
