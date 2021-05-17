from django.http import JsonResponse
import os, time, json, sys, serial, random, datetime


def write_error(name, e):
    feedback=''
    file = './errorlog/errorlog.txt'
    try:
        reader = open(file, 'a')
        message = '{From: '+ str(name)+', Date: ' + str(datetime.datetime.now()) \
                  + ', message: ' + str(e) + '}__error_log__'
        reader.write(f'\n{message}')
    except KeyError as e:
        feedback = {
                'status': 'Invalid request',
                'msg': 'Oops! Technical issue, kindly contact'
                       ' our support desk to report this case. Thanks',
                'classname': 'alert alert-danger p-1 text-center',
            }
    return JsonResponse(feedback, safe=False)