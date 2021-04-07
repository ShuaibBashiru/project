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
            os.unlink('frontend/src/assets/uploaded/coviddataset.csv')
        except:
            print ('ok')
        fs = FileSystemStorage(location='frontend/src/assets/uploaded')
        fs.save(form.name, form)
        print(form)
        res = upload_to_table()
    return JsonResponse(res)


def upload_to_table():
    url = "frontend/src/assets/uploaded/coviddataset.csv"
    data = pd.read_csv(url)
    success = 0
    failed = 0
    counter=0
    for f in data.itertuples():
        counter+=1
        save_record = dataSet()
        save_record.username = 'user_{}'.format(counter)
        save_record.test_date = f.test_date
        save_record.cough = f.cough
        save_record.fever = f.fever
        save_record.sore_throat = f.sore_throat
        save_record.shortness_of_breath = f.shortness_of_breath
        save_record.head_ache = f.head_ache
        save_record.corona_result = f.corona_result
        save_record.age_60_and_above = f.age_60_and_above
        save_record.gender = f.gender
        save_record.test_indication = f.test_indication
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
