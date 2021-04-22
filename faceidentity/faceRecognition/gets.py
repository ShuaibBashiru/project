from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import json
import datetime, time
import random
import csv as cv
import sys
import pyttsx3
import os
import speech_recognition as sr
import openpyxl
import face_recognition
import xlrd
import dlib
import PIL.Image
from PIL import Image
from PIL import ImageFile
import urllib.request
import urllib
import cv2
import numpy as np
import matplotlib as plt
from django.db import connection


def bio_data(request, app_oath):
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM user_profile ORDER BY userid DESC")
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


def courses(request, app_oath):
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT distinct matric, surname, firstname, othername, program, "
                                 "semester FROM course_registration WHERE matric like 'P%' "
                                 "ORDER BY matric DESC")
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
        counter = cursor.execute("SELECT distinct matric, surname, firstname, othername, program, "
                                 "semester FROM course_registration WHERE matric like 'P%' "
                                 "ORDER BY matric DESC")
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
            cam.release()
            cv2.destroyAllWindows()
            return JsonResponse(feedback, safe=False)
        elif k % 256 == 32:
            # SPACE pressed
            user = request.POST['userid']
            newuser = user.replace('/', '')
            img_name = "{}.png".format(newuser)
            cv2.imwrite('frontend/src/assets/passport/' + img_name, frame)
            image = cv2.imread('frontend/src/assets/passport/'+img_name)
            y = 0
            x = 0
            h = 510
            w = 510
            crop_image = image[x:w, y:h]
            cv2.imwrite('frontend/src/assets/passport/' + img_name, crop_image)
            feedback = {
                'status': 'Success',
                'msg': 'Face registered successfully for: {}'.format(user),
                'classname': 'alert alert-primary p-1 text-center',
            }
            cam.release()
            cv2.destroyAllWindows()
            return JsonResponse(feedback, safe=False)

    cam.release()
    cv2.destroyAllWindows()


def match_image(request, app_oath):
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("FACE CAPTURE PANEL")
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
            return JsonResponse(feedback, safe=False)
        elif k % 256 == 32:
            # SPACE pressed
            userid = str(request.POST['userid'])
            newuser = userid.replace('/', '').upper()
            img_name = "{}.png".format(newuser)
            cv2.imwrite('frontend/src/assets/unknown/' + img_name, frame)
            image = cv2.imread('frontend/src/assets/unknown/' + img_name)
            y = 0
            x = 0
            h = 510
            w = 510
            crop_image = image[x:w, y:h]
            cv2.imwrite('frontend/src/assets/unknown/' + img_name, crop_image)

            try:
                known_image = face_recognition.load_image_file('frontend/src/assets/passport/'+img_name)
                unknown_image = face_recognition.load_image_file('frontend/src/assets/unknown/'+img_name)
                known_image_encoding = face_recognition.face_encodings(known_image)[0]
                unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]
                result = face_recognition.compare_faces(
                    [known_image_encoding], unknown_image_encoding, tolerance=0.40)
                # check if it was a match
                if result[0]:
                    with connection.cursor() as cursor:
                        counter = cursor.execute("SELECT * FROM user_profile "
                                                 "WHERE userid=%s", [userid])
                        row = cursor.fetchone()
                        if counter > 0:
                            feedback = {
                                'status': 'Success',
                                'msg': 'Face Matched successfully for Passport: {}'.format(userid),
                                'row': row,
                                'filename': img_name,
                                'classname': 'alert alert-primary p-1 text-center',
                            }
                            cam.release()
                            cv2.destroyAllWindows()
                            return JsonResponse(feedback, safe=False)

                        else:
                            feedback = {
                                'status': 'Failed',
                                'msg': 'Face matched but there is no record from database',
                                'row': "no record",
                                'filename': img_name,
                                'classname': 'alert alert-primary p-1 text-center',
                            }
                            cam.release()
                            cv2.destroyAllWindows()
                            return JsonResponse(feedback, safe=False)

                else:
                    feedback = {
                        'status': 'Failed',
                        'msg': 'Face do not Match, please try again',
                        'row': "no record",
                        'filename': 'avatar.png',
                        'classname': 'alert alert-danger p-1 text-center',
                    }
                    cam.release()
                    cv2.destroyAllWindows()
                    return JsonResponse(feedback, safe=False)

            except Exception as e:
                feedback = {
                    'status': 'Failed',
                    'msg': 'Error classifying image, kindly remove any coverage from your environment.',
                    'row': "no record",
                    'filename': 'avatar.png',
                    'classname': 'alert alert-danger p-1 text-center',
                }
                cam.release()
                cv2.destroyAllWindows()
                print('{}'.format(e))
                return JsonResponse(feedback, safe=False)

    cam.release()
    cv2.destroyAllWindows()


def docket_verifier(request, app_oath):
    userid = str(request.POST['userid'])
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT matric, surname, firstname, othername, program, semester,"
                                     "courseCode, courseTitle, courseUnit FROM course_registration "
                                     "WHERE docketId=%s", [userid])
            row = cursor.fetchall()
            new_userid = str(row[0][0])
            newuser = new_userid.replace('/', '').upper()
            img_name = "{}.png".format(newuser)
            # print(row[0][0])
            if counter > 0:
                feedback = {
                    'status': 'Success',
                    'msg': 'Verified successfully for Matric Number: {}'.format(new_userid),
                    'row': row,
                    'filename': img_name,
                    'classname': 'alert alert-primary p-1 text-center',
                }
                return JsonResponse(feedback, safe=False)

            else:
                feedback = {
                    'status': 'Failed',
                    'msg': 'ID matched but there is no record from database',
                    'row': "no record",
                    'filename': img_name,
                    'classname': 'alert alert-primary p-1 text-center',
                }
                return JsonResponse(feedback, safe=False)

    except Exception as e:
        feedback = {
            'status': 'Failed',
            'msg': 'Error verifying or record does not exist, please try again.',
            'row': "no record",
            'filename': 'avatar.png',
            'classname': 'alert alert-danger p-1 text-center',
        }
        print('{}'.format(e))
    cursor.close()
    return JsonResponse(feedback, safe=False)


def matric_verifier(request, app_oath):
    userid = str(request.POST['userid'])
    newuser = userid.replace('/', '').upper()
    img_name = "{}.png".format(newuser)
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT matric, surname, firstname, othername, program, semester,"
                                     "courseCode, courseTitle, courseUnit FROM course_registration "
                                     "WHERE matric=%s", [userid])
            row = cursor.fetchall()
            if counter > 0:
                feedback = {
                    'status': 'Success',
                    'msg': 'Verified successfully for Matric Number: {}'.format(userid),
                    'row': row,
                    'filename': img_name,
                    'classname': 'alert alert-primary p-1 text-center',
                }
                return JsonResponse(feedback, safe=False)

            else:
                feedback = {
                    'status': 'Failed',
                    'msg': 'ID matched but there is no record from database',
                    'row': "no record",
                    'filename': img_name,
                    'classname': 'alert alert-primary p-1 text-center',
                }
                return JsonResponse(feedback, safe=False)

    except Exception as e:
        feedback = {
            'status': 'Failed',
            'msg': 'Error verifying or record does not exist, please try again.',
            'row': "no record",
            'filename': 'avatar.png',
            'classname': 'alert alert-danger p-1 text-center',
        }
        print('{}'.format(e))
    cursor.close()
    return JsonResponse(feedback, safe=False)


def voice_captured(request, app_oath):
    text = ''
    feedback = ''
    bot = pyttsx3.init()
    bot.setProperty("rate", 178)
    voices = bot.getProperty('voices')
    bot.setProperty('voice', voices[11].id)
    bot.say("Please say your last registered speech, you have five seconds")
    bot.runAndWait()
    with sr.Microphone(device_index=4) as source:
        try:
            speak = sr.Recognizer()
            speak.adjust_for_ambient_noise(source)
            audio = speak.listen(source, timeout=6)
            text = speak.recognize_google(audio)
            print("{}".format(text))
            res = get_voice(request, text)
            print(res)
            bot.say("Your speech mactches an exixsting record. Thanks")
            bot.runAndWait()
            return JsonResponse(res, safe=False)
        except NameError:
            res = "invalid"
            print("Invalid request")
        return JsonResponse(res, safe=False)


def get_voice(request, text):
    with connection.cursor() as cursor:
        counter = cursor.execute("SELECT * FROM voice WHERE voice = %s", [str(text)])
        row = cursor.fetchone()
        if counter > 0:
            print("No record {}".format(text))
            feedback = {
                'status': 'success',
                'msg': 'Your voice is recognized successfully',
                'row': row,
                'text': text
            }
            return feedback
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'Your voice was not matched successfully',
                'row': row,
                'text': text
                 }
            return feedback
        cursor.close()
