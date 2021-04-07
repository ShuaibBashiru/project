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
        username = request.POST['username']
        summary = request.POST['summary']
        notes = request.POST['notes']
        notetitle = request.GET['notetitle']
        try:
            fs = FileSystemStorage(location='frontend/src/assets/uploaded')
            fs.save(form.name, form)
            res = upload_to_table()
        except:
            print("ok")


    return JsonResponse(res)


def upload_to_table():
    url = "frontend/src/assets/uploaded/cropdataset.csv"
    data = pd.read_csv(url)
    success = 0
    failed = 0
    counter=0
    for f in data.itertuples():
        counter+=1
        save_record = dataSet()
        save_record.username = 'user_{}'.format(counter)
        save_record.areaCode = f.areaCode
        save_record.element = f.element
        save_record.itemCode = f.itemCode
        save_record.item = f.item
        save_record.itemYear = f.itemYear
        save_record.unit = f.unit
        save_record.itemValue = f.itemValue
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
