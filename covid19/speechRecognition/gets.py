from django.http import HttpResponse
import pyttsx3
import os
from django.http import JsonResponse
import speech_recognition as sr
from django.core.files.storage import FileSystemStorage
import pandas as pd
import json
from django.http import HttpResponse
import nexmo
import xlwt as exl
from xlwt import Workbook
import openpyxl
import datetime
from django.db import connection


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
