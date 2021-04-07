from django.http import HttpResponse
import pyttsx3
import os
from django.http import JsonResponse
import speech_recognition as sr
from django.core.files.storage import FileSystemStorage
import pandas as pd
import json
from django.http import HttpResponse
import nexmo
import xlwt as exl
from xlwt import Workbook
import openpyxl
import datetime
from .models import BiodataUpload, CoursesUpload
from django.db import connection


def upload(request, app_oath):
    if request.method == 'POST':
        form = request.FILES['image']
        fs = FileSystemStorage(location='frontend/src/assets/uploaded')
        fs.save(form.name, form)
        print(form)
        res = upload_to_table()
    return JsonResponse(res)


def upload_to_table():
    url = "frontend/src/assets/uploaded/studentInfo.csv"
    data = pd.read_csv(url)
    success = 0
    failed = 0
    for f in data.itertuples():
        save_record = BiodataUpload()
        save_record.matric = f.matric
        save_record.passport = f.matric.replace('/', '')+'.png'
        save_record.surname = f.surname
        save_record.firstname = f.firstname
        save_record.othername = f.othername
        save_record.school = f.school
        save_record.department = f.department
        save_record.program = f.program
        save_record.date_time = datetime.datetime.now()
        save_record.save()
        success += 1
    else:
        failed += 1
    if success > 0:
        feedback = {
            'status': 'success',
            'msg': 'Your info was uploaded successfully',
            'classname': 'alert alert-primary p-1 text-center',
        }
    else:
        feedback = {
            'status': 'Failed',
            'msg': 'Your data was not uploaded successfully',
            'classname': 'alert alert-danger p-1 text-center',
        }
    os.unlink('asset/uploaded/studentInfo.csv')
    return feedback
    cursor.close()


def uploadcourses(request, app_oath):
    if request.method == 'POST':
        form = request.FILES['image']
        fs = FileSystemStorage(location='frontend/src/assets/uploaded')
        fs.save(form.name, form)
        print(form)
        res = upload_to_courses()
    return JsonResponse(res)


def upload_to_courses():
    url = "frontend/src/assets/uploaded/courses.csv"
    data = pd.read_csv(url)
    success = 0
    failed = 0
    for f in data.itertuples():
        save_record = CoursesUpload()
        save_record.matric = f.matric
        save_record.surname = f.surname
        save_record.firstname = f.firstname
        save_record.othername = f.othername
        save_record.program = f.program
        save_record.department = f.department
        save_record.school = f.school
        save_record.levelName = f.levelName
        save_record.semester = f.semester
        save_record.sessionName = f.sessionName
        save_record.courseCode = f.courseCode
        save_record.courseTitle = f.courseTitle
        save_record.courseUnit = f.courseUnit
        save_record.docketId = f.docketId
        save_record.date_time = datetime.datetime.now()
        save_record.save()
        success += 1
    else:
        failed += 1
    if success > 0:
        feedback = {
            'status': 'success',
            'msg': 'Your info was uploaded successfully',
            'classname': 'alert alert-primary p-1 text-center',
        }
    else:
        feedback = {
            'status': 'Failed',
            'msg': 'Your data was not uploaded successfully',
            'classname': 'alert alert-danger p-1 text-center',
        }
    os.unlink('frontend/src/assets/uploaded/courses.csv')
    return feedback
    cursor.close()


def send_message(request, app_oath):
    url = "frontend/src/assets/result.csv"
    data = pd.read_csv(url)
    for f in data.itertuples():
        Matric = f.Matric
        Level = f.Level
        Semester = f.Semester
        Phone = f.Phone
        course1 = f.course1
        course2 = f.course2
        course3 = f.course3
        course4 = f.course4
        Gpa = f.Gpa
        Cgpa = f.Cgpa

        client = nexmo.Client(key='da761aac', secret='C9Kibn3r2MMpVaax')
        client.send_message({
            'from': 'YCTResult',
            'to': Phone,
            'text': "{} \n {} \n {} \n {} \n {} \n {} \n {} \n GPA:{} \n CGPA:{} \n".format(Matric, Level, Semester, course1, course2, course3, course4, Gpa, Cgpa)
        })
        return HttpResponse('Sent')

