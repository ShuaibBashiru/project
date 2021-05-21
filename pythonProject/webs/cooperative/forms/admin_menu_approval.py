from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os
import time
import json
import sys
import serial
import random
import datetime
import numpy as np
from django.db import connection, transaction
from authentication.query_columns import dictfetchall
from .admin_menu_models import AddNewMenu
from .admin_menu_models import AddMenuAccess
from authentication.writer import write_error


current_file = 'Admin_Menu_approval_forms'


def check_biodata(request):
    email = request.POST['email']
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT id, email_one FROM admin_record WHERE email_one=%s", [email, ])
        row = dictfetchall(cursor)
        if counter > 0:
            userid = row[0]['id']
            return userid
        else:
            return 0


def check_menu(menuname):
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT id, menuName FROM admin_menus WHERE menuName=%s", [menuname, ])
        row = dictfetchall(cursor)
        if counter > 0:
            menuid = row[0]['id']
            return menuid
        else:
            return 0


def check_access(menuid, userid):
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT id FROM admin_priviledges WHERE menu_id=%s and user_id=%s", [menuid, userid])
        if counter > 0:
            return True
        else:
            return False


def access(request):
    success = 0
    failed = 0
    exist = 0
    no_menu = 0
    total = 0
    if request.method != 'POST':
        feedback = {
            'status': 'Invalid request',
            'statusmsg': 'error',
            'msg': 'Oops! You are making an '
                   'invalid request, kindly refresh '
                   'or check our knowledge base for possible solution.',
            'classname': 'alert-danger',
        }
        return JsonResponse(feedback, safe=False)
    else:
        try:
            biodata = check_biodata(request)
            if biodata == 0:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': 'The account provided does not exist, please confirm and try again.!',
                    'classname': 'alert-danger'
                }
                return JsonResponse(feedback, safe=False)

            else:
                userid = biodata
                lists = list(request.POST['category'].split(','))
                for i in lists:
                    total += 1
                    menuname = i.lower()
                    menuid = check_menu(menuname)
                    if menuid == 0:
                        no_menu += 1
                    else:
                        checkaccess = check_access(menuid, userid)
                        if checkaccess:
                            exist += 1
                        else:
                            gettime = datetime.datetime.now()
                            save_record = AddMenuAccess()
                            save_record.menu_id = menuid
                            save_record.user_id = userid
                            save_record.uniqueCode = int(round(time.time() * 1000))
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
            write_error(current_file, e)

    if success == total:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'msg': 'All record(s) was/were created successfully!',
            'classname': 'alert-primary'
        }

    elif success > 0 and success != total:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'msg': 'Successful! But some record(s) were not processed because '
                   'they might already exist for the selected user, please confirm or try another!',
            'classname': 'alert-warning'
        }
    elif success == 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'msg': 'Your request was not processed because the record(s) already exist(s) for the selected user, '
                   'please confirm or try another.',
            'classname': 'alert-warning'
        }

    else:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong! refresh and try again or contact support',
            'classname': 'alert-danger',
        }

    return JsonResponse(feedback, safe=False)


def update_status(request):
    print('Am here')
    success = 0
    failed = 0
    if request.method != 'POST':
        feedback = {
            'status': 'Invalid request',
            'statusmsg': 'error',
            'msg': 'Oops! You are making an '
                   'invalid request, kindly refresh '
                   'or check our knowledge base for possible solution.',
            'classname': 'alert-danger',
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
            lists = array_id.split(",")
            with connection.cursor() as cursor:
                for keyid in lists:
                    cursor.execute("UPDATE admin_priviledges SET status_id=%s, "
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
            write_error(current_file, e)

    if success > 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'msg': '{} Record updated successfully.'.format(success),
            'classname': 'alert-primary'
        }
    else:
        feedback = {
            'status': 'Failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong or this record no longer exist. '
                   'Kindly confirm this update and try again.',
            'classname': 'alert-danger',
        }

    return JsonResponse(feedback, safe=False)


def delete(request):
    success = 0
    failed = 0
    if request.method != 'POST':
        feedback = {
            'status': 'Invalid request',
            'statusmsg': 'error',
            'msg': 'Oops! You are making an '
                   'invalid request, kindly refresh '
                   'or check our knowledge base for possible solution.',
            'classname': 'alert-danger',
        }
        return JsonResponse(feedback, safe=False)

    else:
        try:
            keyid = request.POST['keyid']
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE admin_priviledges SET status_id=%s, record_status=%s "
                    "WHERE id=%s ", [0, 0, keyid])
                transaction.commit()
                deleted = cursor.rowcount
                if deleted > 0:
                    success += 1
                else:
                    failed += 1
        except Exception as e:
            failed += 1
            write_error(current_file, e)

    if success > 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'msg': 'This record has been deleted and no longer exist,'
                   ' use the menu below to go back.',
            'classname': 'alert-danger'
        }
    else:
        feedback = {
            'status': 'Failed',
            'statusmsg': 'error',
            'msg': 'Oops! This record no longer exist use the menu below to go back.',
            'classname': 'alert-danger',
        }

    return JsonResponse(feedback, safe=False)

