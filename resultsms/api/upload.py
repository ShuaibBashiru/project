from django.http import HttpResponse, JsonResponse
import os
from django.core.files.storage import FileSystemStorage
import pandas as pd
import datetime, json, time
from .models import UploadItemModel

from django.db import connection

def sms_list(request):
    form_name = str(int(round(time.time() * 1000)))
    newform ="{}.csv".format(form_name)
    if request.method == 'POST':
        form = request.FILES['file']
        fs = FileSystemStorage(location='frontend/src/assets/uploaded')
        fs.save(newform, form)
        res = sms_list_func(request, newform)
    return JsonResponse(res)


def sms_list_func(request, newform):
    url = "frontend/src/assets/uploaded/{}".format(newform)
    data = pd.read_csv(url)
    success = 0
    failed = 0
    counter=0
    for f in data.itertuples():
        counter+=1
        save_record = UploadItemModel()
        save_record.surname = f.surname
        save_record.firstname = f.firstname
        save_record.othername = f.othername
        save_record.matric = f.matric
        save_record.levelName = f.levelName
        save_record.semester = f.semester
        save_record.phone = str('0')+str(int(f.phone))
        save_record.courses = f.courses
        save_record.gpa = float(f.gpa)
        save_record.cgpa = float(f.cgpa)
        save_record.program_type = f.program_type
        save_record.date_created = datetime.datetime.now()
        save_record.last_modified = datetime.datetime.now()
        save_record.save()
        success += 1
    else:
        failed += 1
    if success > 0:
        feedback = {
            'status': 'success',
            'confirmed': 'success',
            'msg': 'Your data was uploaded successfully',
            'classname': 'alert alert-primary p-1 text-center',
        }
    else:
        feedback = {
            'status': 'Failed',
            'msg': 'Your data was not uploaded successfully',
            'classname': 'alert alert-danger p-1 text-center',
        }
    return feedback
