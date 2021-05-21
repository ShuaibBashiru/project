from django.db import models


class AddNewAccount(models.Model):
    id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    email_one = models.CharField(max_length=50)
    email_two = models.CharField(max_length=50)
    phone_one = models.CharField(max_length=50)
    phone_two = models.CharField(max_length=50)
    countryCode = models.CharField(max_length=50)
    language_code = models.CharField(max_length=50)
    status_id = models.IntegerField()
    record_status = models.IntegerField()
    created_by = models.IntegerField()
    modified_by = models.IntegerField()
    date_created = models.DateField()
    time_created = models.TimeField()
    date_modified = models.DateField()
    time_modified = models.TimeField()

    class Meta:
        db_table = 'admin_record'


class AddAccount(models.Model):
    id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    businessName = models.CharField(max_length=50)
    businessAddress = models.CharField(max_length=100)
    email_one = models.CharField(max_length=50)
    email_two = models.CharField(max_length=50)
    phone_one = models.CharField(max_length=50)
    phone_two = models.CharField(max_length=50)
    countryCode = models.CharField(max_length=50)
    language_code = models.CharField(max_length=50)
    status_id = models.IntegerField()
    record_status = models.IntegerField()
    created_by = models.IntegerField()
    modified_by = models.IntegerField()
    date_created = models.DateField()
    time_created = models.TimeField()
    date_modified = models.DateField()
    time_modified = models.TimeField()

    class Meta:
        db_table = 'business_record'
