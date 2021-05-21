from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import datetime
import time
import json
import sys
import serial
import string
import random
import numpy as np
from django.db import connection, transaction
from .admin_account_models import AddNewAccount
from authentication.writer import write_error
from mailer.newpassword_mailer import new_password_mailer


def addNew(request):
    success = 0
    failed = 0
    business_name = request.POST['businessName']
    email = request.POST['email']
    letters = string.ascii_lowercase
    code = ''.join(random.choice(letters) for i in range(8))
    if request.method != 'POST':
        feedback = {
                'status': 'Invalid request',
                'msg': 'Oops! You are making an '
                       'invalid request, kindly refresh '
                       'or check our knowledge base for possible solution.',
                'classname': 'alert-danger',
            }
        return JsonResponse(feedback, safe=False)

    else:
        try:
            gettime = datetime.datetime.now()
            save_record = AddNewAccount()
            save_record.surname = request.POST['surname']
            save_record.firstname = request.POST['firstname']
            save_record.language_code = request.POST['languageCode']
            save_record.email_one = request.POST['email']
            save_record.email_two = request.POST['email']
            save_record.phone_one = request.POST['phone']
            save_record.phone_two = request.POST['phone']
            save_record.created_by = 0
            save_record.modified_by = 0
            save_record.status_id = 0
            save_record.record_status = 1
            save_record.date_created = str(datetime.date.today())
            save_record.time_created = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
            save_record.date_modified = str(datetime.date.today())
            save_record.time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
            save_record.save()
            success = 1

        except Exception as e:
            success = 0
            write_error('New account', e)

    if success > 0:
        res = new_password_mailer(email, business_name, code)
        if res is True:
            feedback = {
                'status': 'success',
                'statusmsg': 'success',
                'msg': 'New record was created successfully! now redirecting..',
                'redirect': '/site/newpassword/' + str(request.POST['email']).lower() + '/' + code,
                'classname': 'alert-primary'
            }

        else:
            feedback = {
                'status': 'failed',
                'statusmsg': 'error',
                'msg': 'We could not process mail notification request right now, please try again later',
                'classname': 'alert-danger',
            }
    else:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong! It is like this record already exist, '
                   'Kindly check our knowledge base for possible solution.',
            'classname': 'alert-danger',
        }

    return JsonResponse(feedback, safe=False)
