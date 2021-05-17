from django.http import HttpResponse, JsonResponse
import speech_recognition as sr
from django.core.files.storage import FileSystemStorage
import pandas as pd
import json, time
import os, datetime
from .models import fileUpload

def upload(request):
    filename=str(int(round(time.time() * 1000)))
    if request.method == 'POST':
        form = request.FILES['image']

        try:
            fs = FileSystemStorage(location='frontend/src/assets/uploaded')
            fs.save(filename+'.pdf', form)
            save_record = fileUpload()
            save_record.user_id = str(int(round(time.time() * 2000)))
            save_record.file_title = request.POST['notetitle']
            save_record.file_name = filename
            save_record.date_created = datetime.datetime.now()
            save_record.last_modified = datetime.datetime.now()
            save_record.save()

            feedback = {
                'status': 'success',
                'msg': 'Your info was uploaded successfully',
                'classname': 'alert alert-primary p-1 text-center',
            }
        except Exception as e:
            print(e)
            feedback = {
                'status': 'Failed',
                'msg': 'Something went wrong, refresh and try again',
                'classname': 'alert alert-danger p-1 text-center',
            }
    else:
        feedback = {
            'status': 'Failed',
            'msg': 'Invalid request, refresh and try again',
            'classname': 'alert alert-danger p-1 text-center',
        }

    return JsonResponse(feedback, safe=False)
