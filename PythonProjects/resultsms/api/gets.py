from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import json
import datetime, time
from numpy import random
import sys, os, urllib
import openpyxl
import numpy as np
import matplotlib as plt
from django.db import connection


def get_sms_list(request):
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM result_tbl "
                                    "ORDER BY matric asc")
        row = cursor.fetchall()
        if counter > 0:
            feedback = {
                'status': 'success',
                'confirmed': 'success',
                'msg': 'Records are listed below',
                'result': row,
                'classname': 'alert alert-primary p-1 text-center',
            }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'No record(s) found',
                'classname': 'alert alert-danger p-1 text-center',
                 }
        return JsonResponse(feedback, safe=False)
        cursor.close()


def get_sms_list_select(request):
    levelName = request.GET['levelName']
    semester = request.GET['semester']
    program_type = request.GET['program_type']
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM result_tbl WHERE levelName=%s "
                                 "AND semester=%s AND program_type=%s "
                                    "ORDER BY matric ASC", [levelName, semester, program_type])
        row = cursor.fetchall()
        if counter > 0:
            feedback = {
                'status': 'success',
                'confirmed': 'success',
                'msg': 'Records are listed below',
                'result': row,
                'classname': 'alert alert-primary p-1 text-center',
            }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'No record(s) found',
                'classname': 'alert alert-danger p-1 text-center',
                 }
        return JsonResponse(feedback, safe=False)
        cursor.close()


def send_sms(request):
    counter = 0
    levelName = request.GET['levelName']
    semester = request.GET['semester']
    program_type = request.GET['program_type']
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT matric, levelName, semester, phone, courses, gpa, cgpa FROM result_tbl WHERE levelName=%s "
                                 "AND semester=%s AND program_type=%s "
                                    "ORDER BY matric ASC LIMIT 3", [levelName, semester, program_type])
        row = cursor.fetchall()

        for f in row:
            counter+=1
            matric = f[0]
            levelName = f[1]
            semester = f[2]
            phone = f[3]
            courses = f[4]
            gpa = f[5]
            cgpa = f[6]
            print(f[3])
            message= "[{}]__[{}]__[{}]__[{}]__[GPA:{}] -- [CGPA:{}] ".format(matric, levelName, semester, courses, gpa, cgpa)
            start_url = "https://portal.nigeriabulksms.com/api/?username=instructsme@gmail.com&password=Ayodele123.&message="+str(message)+"&sender=Yctresult' &mobiles="+str(phone)+""
            url = start_url.replace(" ", "")
            urllib.request.urlopen(url)
            # print(weburl.getcode)
        if counter > 0:
            feedback = {
                'status': 'success',
                'confirmed': 'success',
                'msg': 'Message successfully sent. Good Job!',
                'result': row,
                'classname': 'alert alert-primary p-1 text-center',
            }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'Error sending message, please try again',
                'classname': 'alert alert-danger p-1 text-center',
                 }
        return JsonResponse(feedback, safe=False)
        cursor.close()
