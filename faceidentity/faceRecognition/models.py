from django.db import models


class BiodataUpload(models.Model):
    userid = models.CharField(max_length=100)
    passport = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    othername = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    date_time = models.DateTimeField(max_length=100)

    class Meta:
        db_table = 'user_profile'


class CoursesUpload(models.Model):
    matric = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    othername = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    levelName = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    sessionName = models.CharField(max_length=100)
    courseCode = models.CharField(max_length=100)
    courseTitle = models.CharField(max_length=100)
    courseUnit = models.CharField(max_length=100)
    docketId = models.CharField(max_length=100)
    date_time = models.DateTimeField(max_length=100)

    class Meta:
        db_table = 'course_registration'


class Person(models.Model):
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    othername = models.DateField(max_length=100)


class VoiceRegistration(models.Model):
    username = models.CharField(max_length=100)
    voice = models.CharField(max_length=100)
    date_time = models.DateTimeField(max_length=100)

    class Meta:
        db_table = 'voice'
        managed = False