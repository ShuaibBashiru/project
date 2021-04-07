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


def upload(request, app_oath):
    if request.method == 'POST':
        form = request.FILES['image']
        fs = FileSystemStorage(location='asset')
        fs.save(form.name, form)
        print(form)
    return HttpResponse("Worked")


def csv_reader(request, app_oath):
    url = "asset/result.csv"
    data = pd.read_csv(url)
    json_str = data.to_json()
    print(data)
    return JsonResponse(json_str, safe=False)


def send_message(request, app_oath):
    url = "asset/result.csv"
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

# def bio_data(request, app_oath):
#     for p in Person.objects.raw('SELECT * FROM studentinfo LIMIT 1'):
#         print(p.surname)
#     return JsonResponse(p, safe=False)