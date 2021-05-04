from django.db import models


class VoiceRegistration(models.Model):
    username = models.CharField(max_length=100)
    voice = models.CharField(max_length=100)
    date_time = models.DateTimeField(max_length=100)

    class Meta:
        db_table = 'voice'
        managed = False


# class GetVoice(models.Model):
#     username = models.CharField(max_length=100)
#     v1 = models.CharField(max_length=100)
#     v2 = models.CharField(max_length=100)
#     v3 = models.CharField(max_length=100)
#     date_time = models.DateTimeField(max_length=100)
#
#     class Meta:
#         db_table = 'voice_table'
# Create your models here.
