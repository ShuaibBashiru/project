from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os, time, json, sys, serial, random, datetime
import numpy as np
from django.db import connection, transaction
from .models import AddWidget
from authentication.writer import write_error


def add_widget(request):
    success = 0
    failed = 0
    if request.method != 'POST':
        feedback = {
                'status': 'Invalid request',
                'msg': 'Oops! You are making an '
                       'invalid request, kindly refresh '
                       'or check our knowledge base for possible solution.',
                'classname': 'alert alert-danger p-1 text-center',
            }
        return JsonResponse(feedback, safe=False)

    else:
        try:
            gettime = datetime.datetime.now()
            save_record = AddWidget()
            save_record.widgetName=request.POST['widget']
            save_record.widgetTitle=request.POST['title']
            save_record.uniqueCode=int(round(time.time() * 1000))
            save_record.created_by = request.session['userdata']['id']
            save_record.modified_by = request.session['userdata']['id']
            save_record.status_id = 0
            save_record.record_status = 1
            save_record.date_created = str(datetime.date.today())
            save_record.time_created = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
            save_record.date_modified = str(datetime.date.today())
            save_record.time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
            save_record.save()
            success += 1
        except Exception as e:
            failed += 1
            write_error('Widget', e)

    if success > 0:
        feedback = {
            'status': 'success',
            'confirmed': 'success',
            'msg': 'New record was created successfully! '
                   'Please note that this record is not yet active '
                   'until you activate it on Record'"s'" ' page.',
            'classname': 'alert alert-primary p-1 text-center'
        }
    else:
        feedback = {
            'status': 'Failed',
             'msg': 'Something went wrong! It is like this record already exist, '
                    'kindly check our knowledge base for possible solution.',
            'classname': 'alert alert-danger p-1 text-center',
        }

    return JsonResponse(feedback, safe=False)


def update_widget(request):
    success = 0
    failed = 0
    if request.method != 'POST':
        feedback = {
            'status': 'Invalid request',
            'msg': 'Oops! You are making an '
                   'invalid request, kindly refresh '
                   'or check our knowledge base for possible solution.',
            'classname': 'alert alert-danger p-1 text-center',
        }
        return JsonResponse(feedback, safe=False)

    else:
        try:
            gettime = datetime.datetime.now()
            date_modified = str(datetime.date.today())
            time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
            modified_by = request.session['userdata']['id']
            widgetTitle = request.POST['title']
            status_id = 0
            keyid = request.POST['keyid']
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE user_widgets SET widgetTitle=%s, status_id=%s, "
                    "modified_by=%s, date_modified=%s, time_modified=%s "
                    "WHERE uniqueCode=%s ",
                    [widgetTitle, status_id, modified_by, date_modified, time_modified, keyid])
                transaction.commit()
                updated = cursor.rowcount
                if updated > 0:
                    success += 1
                else:
                    failed += 1
        except Exception as e:
            failed += 1
            write_error('Widget', e)

    if success > 0:
        feedback = {
            'status': 'success',
            'confirmed': 'success',
            'msg': 'Record updated successfully.',
            'classname': 'alert alert-primary p-1 text-center'
        }
    else:
        feedback = {
            'status': 'Failed',
             'msg': 'Something went wrong or this record no longer exist. '
                    'Kindly confirm this update and try again.',
            'classname': 'alert alert-danger p-1 text-center',
        }

    return JsonResponse(feedback, safe=False)


def update_widget_status(request):
    success = 0
    failed = 0
    if request.method != 'POST':
        feedback = {
                'status': 'Invalid request',
                'msg': 'Oops! You are making an '
                       'invalid request, kindly refresh '
                       'or check our knowledge base for possible solution.',
                'classname': 'alert alert-danger p-1 text-center',
            }
        return JsonResponse(feedback, safe=False)

    else:
        try:
            gettime = datetime.datetime.now()
            date_modified = str(datetime.date.today())
            time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
            modified_by = request.session['userdata']['id']
            status_id = request.POST['listStatus']
            array_id = request.POST['keyid']
            lists=array_id.split(",")
            with connection.cursor() as cursor:
                for keyid in lists:
                    cursor.execute("UPDATE user_widgets SET status_id=%s, "
                                   "modified_by=%s, date_modified=%s, "
                                   "time_modified=%s WHERE id=%s ",
                                   [status_id, modified_by, date_modified, time_modified, keyid])
                    transaction.commit()
                    updated = cursor.rowcount
                    if updated > 0:
                        success += 1
                    else:
                        failed += 1
        except Exception as e:
            failed += 1
            write_error('Widget', e)

    if success > 0:
        feedback = {
            'status': 'success',
            'confirmed': 'success',
            'msg': '{} Record updated successfully.'.format(success),
            'classname': 'alert alert-primary p-1 text-center'
        }
    else:
        feedback = {
            'status': 'Failed',
             'msg': 'Something went wrong or this record no longer exist. '
                    'Kindly confirm this update and try again.',
            'classname': 'alert alert-danger p-1 text-center',
        }

    return JsonResponse(feedback, safe=False)


def delete_widget(request):
    success = 0
    failed = 0
    if request.method != 'POST':
        feedback = {
            'status': 'Invalid request',
            'msg': 'Oops! You are making an '
                   'invalid request, kindly refresh '
                   'or check our knowledge base for possible solution.',
            'classname': 'alert alert-danger p-1 text-center',
        }
        return JsonResponse(feedback, safe=False)

    else:
        try:
            keyid = request.POST['keyid']
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE user_widgets SET status_id=%s, record_status=%s "
                    "WHERE uniqueCode=%s ", [0, 0, keyid])
                transaction.commit()
                deleted = cursor.rowcount
                if deleted > 0:
                    success += 1
                else:
                    failed += 1
        except Exception as e:
            failed += 1
            write_error('Widget', e)

    if success > 0:
        feedback = {
            'status': 'success',
            'confirmed': 'success',
            'msg': 'This record has been deleted and no longer exist,'
                   ' use the menu below to go back.',
            'classname': 'alert alert-danger p-1 text-center'
        }
    else:
        feedback = {
            'status': 'Failed',
             'msg': 'Oops! This record no longer exist'
                    'use the menu below to go back.',
            'classname': 'alert alert-danger p-1 text-center',
        }

    return JsonResponse(feedback, safe=False)



