from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import json
import datetime, time
import random
import sys, os
import openpyxl
import numpy as np
import matplotlib as plt
from django.db import connection


def get_dataset(request):
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM crop_list "
                                    "ORDER BY itemYear DESC")
        row = cursor.fetchall()
        if counter > 0:
            feedback = {
                'res': True,
                'status': 'success',
                'msg': 'Records are listed below',
                'row': row,
                'classname': 'alert alert-primary p-1 text-center',
            }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'No data uploaded yet',
                'row': row,
                'classname': 'alert alert-danger p-1 text-center',
                 }
        return JsonResponse(feedback, safe=False)
        cursor.close()


def listsummary(request):
    username = request.GET['username']
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT username, notetitle, notes, summary, date_created FROM text_summary_tbl "
                                     "WHERE username=%s"
                                     "ORDER BY id DESC", [username, ])
            row = cursor.fetchall()
            if counter > 0:
                feedback = {
                    'res': True,
                    'status': 'success',
                    'msg': 'Records are listed below',
                    'row': row,
                    'classname': 'alert alert-primary p-1 text-center',
                }
            else:
                feedback = {
                    'status': 'Failed',
                    'msg': 'No data uploaded yet',
                    'row': row,
                    'classname': 'alert alert-danger p-1 text-center',
                }
    except Exception as e:
        feedback = {
            'status': 'Failed',
            'msg': 'Error processing your rrequest, please try again',
            'classname': 'alert alert-danger p-1 text-center',
        }
        print(e)

    return JsonResponse(feedback, safe=False)
    cursor.close()
