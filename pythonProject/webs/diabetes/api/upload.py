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
from .models import dataSet
from django.db import connection


def upload(request):
    if request.method == 'POST':
        form = request.FILES['image']
        try:
            os.unlink('frontend/src/assets/uploaded/diabetes.csv')
        except:
            print ('ok')
        fs = FileSystemStorage(location='frontend/src/assets/uploaded')
        fs.save(form.name, form)
        print(form)
        res = upload_to_table()
    return JsonResponse(res)


def upload_to_table():
    url = "frontend/src/assets/uploaded/diabetes.csv"
    data = pd.read_csv(url)
    success = 0
    failed = 0
    counter=0
    for f in data.itertuples():
        counter+=1
        save_record = dataSet()
        save_record.username = 'user_{}'.format(counter)
        save_record.glucose = f.glucose
        save_record.bloodPressure = f.Bp
        save_record.skinThickness = f.skinThickness
        save_record.insulin = f.insulin
        save_record.bmi = f.bmi
        save_record.diabetesPedigreeFunction = f.pedigreeFunction
        save_record.age = f.age
        save_record.outcome = f.outcome
        save_record.date_created = datetime.datetime.now()
        save_record.last_modified = datetime.datetime.now()
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
    return feedback
