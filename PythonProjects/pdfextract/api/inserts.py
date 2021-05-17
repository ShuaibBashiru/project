from django.http import HttpResponse, JsonResponse
import pyttsx3
import os
import pandas as pd
import json
import datetime
from .models import Summary_note
import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
#
# username = request.GET['username']
# summarynote = request.GET['summarynote']
# notetitle = request.GET['notetitle']

def summarize(request):
    notes = request.GET['notes']
    success = 0
    failed = 0
    counter = 0
    output = ""
    text= """
    {}
    """.format(notes)
    try:
        stopWords = set(stopwords.words('english'))
        words = word_tokenize(text)
        freqTable = dict()
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1

        # create dict to keep the score of each sentence
        sentences = sent_tokenize(text)
        sentenceValue = dict()

        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq

        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]

        average = int(sumValues / len(sentenceValue))

        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > 1.2 * average):
                summary += " " + sentence
        output = summary

        feedback = {
            'status': 'success',
            'msg': 'Your request was successfully, check the result below',
            'classname': 'alert alert-primary p-1 text-center',
            'result': output,
            'originalLenght': len(notes),
            'summaryLenght': len(output),
            }
    except Exception as e:
        feedback = {
            'status': 'Failed',
            'msg': 'Your request was not successful or your document could not be summarized, please try again with detailed document',
            'classname': 'alert alert-danger p-1 text-center',
        }
    return JsonResponse(feedback, safe=False)

def savesummary(request):
    username = request.GET['username']
    summary = request.GET['summary']
    notes = request.GET['notes']
    notetitle = request.GET['notetitle']
    success = 0
    failed = 0
    counter = 0
    try:
        save_record = Summary_note()
        save_record.username = username
        save_record.notes = notes
        save_record.notetitle = notetitle
        save_record.summary = summary
        save_record.date_created = datetime.datetime.now()
        save_record.last_modified = datetime.datetime.now()
        save_record.save()
        success += 1
    except Exception as e:
        failed += 1
        print(e)
    if success > 0:
        feedback = {
            'status': 'success',
            'msg': 'Your request was successful',
            'classname': 'alert alert-primary p-1 text-center',
        }
    else:
        feedback = {
            'status': 'Failed',
            'msg': 'Your request was not successful, please try again',
            'classname': 'alert alert-danger p-1 text-center',
        }
    return JsonResponse(feedback, safe=False)