from django.db import models

# Create your models here.
class CreateAccount(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    othername = models.CharField(max_length=50)
    email_one = models.CharField(max_length=50)
    phone_one = models.CharField(max_length=50)
    persional_id = models.CharField(max_length=50)
    iteration = models.CharField(max_length=50)
    runtime = models.CharField(max_length=50)
    other = models.CharField(max_length=50)
    date_created = models.CharField(max_length=50)

    class Meta:
        db_table = 'user_record'
    