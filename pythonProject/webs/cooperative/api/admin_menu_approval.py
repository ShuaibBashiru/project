import sys, os
from django.http import HttpResponse, JsonResponse
import json, datetime, time
from numpy import random
import numpy as np
import pandas as pd
import csv
import urllib.request
from django.db import connection
from authentication.query_columns import dictfetchall
from authentication.writer import write_error
import pickle
import base64

current_file = "Admin_Approval_list"


def list(request):
    try:
        getlimit = int(request.GET['limitTo'])
        if int(getlimit) == 1:
            limitTo = 18446744073709551615
            offset = 0
        else:
            limitTo = int(request.GET['limitTo'])
            offset = 0

        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT t2.id, t2.status_id, t0.email_one, t1.category, t1.menuName, t1.menu_description, "
                                     "t1.menu_icon, t1.uniqueCode, t2.date_modified, t2.time_modified FROM "
                                     "admin_menus as t1 INNER JOIN admin_priviledges as t2 "
                                     "ON t1.id=t2.menu_id INNER JOIN admin_record as t0 on t0.id = t2.user_id "
                                     "WHERE t1.record_status=%s AND t1.status_id=%s AND "
                                     "t2.record_status=%s "
                                     "ORDER BY t2.time_modified, t2.date_modified, t2.status_id LIMIT %s OFFSET %s ",
                                     [1, 1, 1, limitTo, offset])

            row = dictfetchall(cursor)
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': row,
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'msg': 'You are yet to add any record here, kindly use the New menu button to create one.',
                    'classname': '',
                }

    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'msg': 'Something went wrong, kindly reload this page.',
            'classname': 'alert-danger',
        }
    finally:
        cursor.close()
    return JsonResponse(feedback, safe=False)


def list_filter(request):
    try:
        statusid = request.GET['status_id']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT t2.id, t2.status_id, t0.email_one, t1.category, t1.menuName, t1.menu_description, "
                                     "t1.menu_icon, t1.uniqueCode, t2.date_modified, t2.time_modified FROM "
                                     "admin_menus as t1 INNER JOIN admin_priviledges as t2 "
                                     "ON t1.id=t2.menu_id INNER JOIN admin_record as t0 on t0.id = t2.user_id "
                                     "WHERE t1.record_status=%s AND t1.status_id=%s AND "
                                     "t2.record_status=%s AND t2.status_id=%s "
                                     "ORDER BY t2.time_modified, t2.date_modified, t2.status_id",
                                     [1, 1, 1, statusid])

            row = dictfetchall(cursor)
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': row,
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'msg': 'There is no record for your search, try another or'
                           ' use the New menu button to create one.',
                    'classname': '',
                }
    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'msg': 'Something went wrong, kindly reload this page.',
            'classname': 'alert-danger',
        }
    finally:
        cursor.close()
    return JsonResponse(feedback, safe=False)


def list_search(request):
    try:
        search = request.GET['search']
        with connection.cursor() as cursor:

            counter = cursor.execute("SELECT t2.id, t2.status_id, t0.email_one, t1.category, t1.menuName, t1.menu_description, "
                                     "t1.menu_icon, t1.uniqueCode, t2.date_modified, t2.time_modified FROM "
                                     "admin_menus as t1 INNER JOIN admin_priviledges as t2 "
                                     "ON t1.id=t2.menu_id INNER JOIN admin_record as t0 on t0.id = t2.user_id "
                                     "WHERE t1.record_status=%s AND t1.status_id=%s AND "
                                     "t2.record_status=%s AND (t0.email_one=%s OR t1.menuName=%s OR "
                                     "t1.menu_description=%s ) "
                                     "ORDER BY t2.time_modified, t2.date_modified, t2.status_id",
                                     [1, 1, 1, search, search, search])
            row = dictfetchall(cursor)
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': row,
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'msg': 'There is no record for your search,'
                           ' try another or use the New menu button to create one.',
                    'classname': '',
                }
    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'msg': 'Something went wrong, kindly reload this page.',
            'classname': 'alert-danger',
        }
    finally:
        cursor.close()
    return JsonResponse(feedback, safe=False)


def preview(request):
    try:
        keyid = request.GET['keyid']
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT * FROM admin_menus WHERE record_status=%s AND id=%s"
                                     "ORDER BY time_modified, date_modified, status_id ", [1, keyid])
            row = dictfetchall(cursor)
            if counter > 0:
                data = {
                    'keyid': row[0]['uniqueCode'],
                    'widgetName': row[0]['widgetName'],
                    'widgetTitle': row[0]['widgetTitle'],
                }
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': data,
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'msg': 'Something went wrong or this record no longer exist. '
                           'Kindly confirm this update and try again.',
                    'classname': '',
                }
    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'msg': 'Something went wrong, kindly reload this page or try again.',
            'classname': 'alert-danger',
        }
    finally:
        cursor.close()
    return JsonResponse(feedback, safe=False)


def download(request):
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT t0.email_one, t1.category, t1.menuName, t1.menu_description, "
                                     "t1.menu_icon, t1.uniqueCode, t2.status_id, t2.date_modified, t2.time_modified FROM "
                                     "admin_menus as t1 INNER JOIN admin_priviledges as t2 "
                                     "ON t1.id=t2.menu_id INNER JOIN admin_record as t0 on t0.id = t2.user_id "
                                     "WHERE t1.record_status=%s AND t1.status_id=%s AND "
                                     "t2.record_status=%s "
                                     "ORDER BY t2.time_modified, t2.date_modified, t2.status_id ",
                                     [1, 1, 1])

            row = dictfetchall(cursor)
            df = pd.DataFrame(row)
            gettime = datetime.datetime.now()
            date_modified = str(datetime.date.today())
            time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
            filename = '{}_{}_{}.csv'.format(current_file, date_modified, time_modified)
            df.to_csv('assets/reports/' + filename)
            with open("assets/reports/" + filename, "rb") as img_file:
                my_string = base64.b64encode(img_file.read())
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': 'Your file is ready for download, click the button below',
                    'result': '',
                    'baseData': str('data:text/csv;base64, ' + my_string.decode('utf-8')),
                    'baseDataname': str(filename),
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'msg': 'There is no record to download,'
                           ' use the New menu button to create one.',
                    'classname': '',
                }
    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'msg': 'Something went wrong, kindly reload this page.',
            'classname': 'alert-danger',
        }
    finally:
        cursor.close()
    return JsonResponse(feedback, safe=False)
