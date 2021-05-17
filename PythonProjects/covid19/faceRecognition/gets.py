from django.http import HttpResponse
import pyttsx3
from django.http import JsonResponse
import speech_recognition as sr
from django.core.files.storage import FileSystemStorage
import pandas as pd
import json
from django.http import HttpResponse
import nexmo
import datetime
import random
import csv as cv
import matplotlib
import matplotlib.pyplot as plt
import sys
import os, time, serial
import face_recognition
import xlrd
import dlib
import PIL.Image
from PIL import ImageFile
import urllib.request
import urllib
import cv2
import numpy as np

import time
from django.db import connection


def bio_data(request, app_oath):
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM passports")
        row = cursor.fetchall()
        if counter > 0:
            feedback = {
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


def courses(request, app_oath):
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM course_registration LIMIT 100")
        row = cursor.fetchall()
        if counter > 0:
            feedback = {
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


def listdataface(request, app_oath):
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM studentinfo")
        row = cursor.fetchall()
        if counter > 0:
            feedback = {
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


def capturephoto(request, app_oath):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("FACE CAPTURE PANEL")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("FACE CAPTURE PANEL", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            feedback = {
                'status': 'Failed',
                'msg': 'Enrollment was interrupted, try again',
                'classname': 'alert alert-danger p-1 text-center',
            }
            break
        elif k % 256 == 32:
            # SPACE pressed
            user = request.POST['userid']
            newuser = user.replace('/', '')
            img_name = "{}.png".format(newuser)
            cv2.imwrite('frontend/src/assets/passport/' + img_name, frame)
            feedback = {
                'status': 'Success',
                'msg': 'Face registered successfully for: {}'.format(user),
                'classname': 'alert alert-primary p-1 text-center',
            }
            break

    cam.release()
    cv2.destroyAllWindows()
    return JsonResponse(feedback, safe=False)


def match_image(request, app_oath):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("FACE CAPTURE PANEL")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("FACE CAPTURE", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            feedback = {
                'status': 'Failed',
                'msg': 'Enrollment was interrupted, try again',
                'classname': 'alert alert-danger p-1 text-center',
            }
            break
        elif k % 256 == 32:
            # SPACE pressed
            userid = str(request.POST['userid'])
            newuser = userid.replace('/', '').upper()
            img_name = "{}.png".format(newuser)
            cv2.imwrite('frontend/src/assets/unknown/' + img_name, frame)
            positive = 0
            negative = 0
            # load your image
            try:
                known_image = face_recognition.load_image_file('frontend/src/assets/passport/'+img_name)
                unknown_image = face_recognition.load_image_file('frontend/src/assets/unknown/'+img_name)
                known_image_encoding = face_recognition.face_encodings(known_image)[0]
                unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]
                result = face_recognition.compare_faces(
                    [known_image_encoding], unknown_image_encoding, tolerance=0.40)
            except Exception as e:
                feedback = {
                    'status': 'Failed',
                    'msg': 'Error classifying image, kindly remove any coverage from your face.',
                    'row': "no record",
                    'filename': '../assets/passport/{}'.format(img_name),
                    'classname': 'alert alert-danger p-1 text-center',
                }
                print('{}'.format(e))
                break
            # check if it was a match
            if result[0]:
                positive += 1
                filename = newuser
            else:
                negative += 1

            if positive > negative:
                with connection.cursor() as cursor:
                    counter = cursor.execute("SELECT c.* FROM course_registration c WHERE c.matric=%s", [userid])
                    row = cursor.fetchone()
                    if counter > 0:

                        feedback = {
                            'status': 'Success',
                            'msg': 'Face Matched successfully',
                            'row': row,
                            'filename': img_name,
                            'classname': 'alert alert-primary p-1 text-center',
                        }
                        break
                    else:
                        feedback = {
                            'status': 'Failed',
                            'msg': 'Face matched but there is no record from database',
                            'row': "no record",
                            'filename': img_name,
                            'classname': 'alert alert-primary p-1 text-center',
                        }
                        break
            else:
                feedback = {
                    'status': 'Failed',
                    'msg': 'Face do not Matched',
                    'classname': 'alert alert-danger p-1 text-center',
                }
                break
    cam.release()
    cv2.destroyAllWindows()
    return JsonResponse(feedback, safe=False)


def match_image_external(request, app_oath):
    cam = cv2.VideoCapture(1)
    cv2.namedWindow("FACE CAPTURE PANEL")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("FACE CAPTURE", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            feedback = {
                'status': 'Failed',
                'msg': 'Enrollment was interrupted, try again',
                'classname': 'alert alert-danger p-1 text-center',
            }
            break
        elif k % 256 == 32:
            # SPACE pressed
            userid = str(request.POST['userid'])
            newuser = userid.replace('/', '').upper()
            img_name = "{}.png".format(newuser)
            cv2.imwrite('frontend/src/assets/unknown/' + img_name, frame)
            positive = 0
            negative = 0
            filename = ''
            # load your image
            img1 = 'frontend/src/assets/passport/'+img_name
            img2 = 'frontend/src/assets/unknown/'+img_name
            try:
                known_image = face_recognition.load_image_file(img1)
                unknown_image = face_recognition.load_image_file(img2)
                known_image_encoding = face_recognition.face_encodings(known_image)[0]
                unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]
                result = face_recognition.compare_faces(
                    [known_image_encoding], unknown_image_encoding, tolerance=0.40)
            except Exception as e:
                feedback = {
                    'status': 'Failed',
                    'msg': 'Error classifying image, kindly remove any coverage from your face.',
                    'row': "no record",
                    'filename': '../assets/passport/{}'.format(img_name),
                    'classname': 'alert alert-danger p-1 text-center',
                }
                print(e)
                break
            # check if it was a match
            if result[0]:
                positive += 1
                filename = newuser
            else:
                negative += 1

            if positive > negative:
                with connection.cursor() as cursor:
                    counter = cursor.execute("SELECT c.* FROM course_registration c"
                                             "WHERE c.matric=%s", [userid])
                    row = cursor.fetchone()
                    if counter > 0:
                        feedback = {
                            'status': 'Success',
                            'msg': 'Face Matched successfully',
                            'row': row,
                            'filename': '../assets/passport/{}'.format(img_name),
                            'classname': 'alert alert-primary p-1 text-center',
                        }
                        break
                    else:
                        feedback = {
                            'status': 'Failed',
                            'msg': 'Face matched but there is no record from database',
                            'row': "no record",
                            'filename': '../assets/passport/{}'.format(img_name),
                            'classname': 'alert alert-primary p-1 text-center',
                        }
                        break
            else:
                feedback = {
                    'status': 'Failed',
                    'msg': 'Face do not Matched',
                    'classname': 'alert alert-danger p-1 text-center',
                }
                break
    cam.release()
    cv2.destroyAllWindows()
    return JsonResponse(feedback, safe=False)


# def facecapture():
#     imgRes = urllib.request.urlopen(url)
#     imgNp = np.array(bytearray(imgRes.read()), dtype=np.uint8)
#     img = cv2.imdecode(imgNp, -1)
#     cv2.imshow("Web camera", img)
#     cv2.waitKey(10)
#     feedback = {
#         'success': 'success'
#     }
#     return JsonResponse(feedback, safe=False)
# import os
# folder = 'test'
# os.mkdir(folder)
# # use opencv to do the job
# import cv2
# print(cv2.__version__)  # my version is 3.1.0
# vidcap = cv2.VideoCapture('test_video.mp4')
# count = 0
# while True:
#     success,image = vidcap.read()
#     if not success:
#         break
#     cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
#     count += 1
# print("{} images are extacted in {}.".format(count,folder))