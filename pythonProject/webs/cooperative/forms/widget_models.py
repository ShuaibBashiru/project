from django.db import models


class AddNewWidget(models.Model):
    id = models.AutoField(primary_key=True)
    widgetName = models.CharField(max_length=50)
    widgetTitle = models.CharField(max_length=100)
    uniqueCode = models.CharField(max_length=50)
    status_id = models.IntegerField()
    record_status = models.IntegerField()
    created_by = models.IntegerField()
    modified_by = models.IntegerField()
    date_created = models.DateField()
    time_created = models.TimeField()
    date_modified = models.DateField()
    time_modified = models.TimeField()

    class Meta:
        db_table = 'user_widgets'
