from django.http import HttpResponse, JsonResponse
import speech_recognition as sr
from django.core.files.storage import FileSystemStorage
import pandas as pd
import json, time
import os, datetime
from .models import fileUpload
from PyPDF2 import PdfFileReader, PdfFileMerger
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
from fpdf import FPDF
from pdf2docx import parse
from docx import Document
import subprocess

# import unicode_normalize
import sys
def file_extract(request):
    filelist = []
    merger = PdfFileMerger()
    try:
        if request.method == 'POST':
            file_location = 'frontend/src/assets/uploaded/'+str(request.POST['filename'])+'.pdf'
            new_location = 'frontend/src/assets/file_preprocess/'
            file_dir = 'frontend/src/assets/extracted/'
            file_final_name = str(int(round(time.time() * 2000)))

            filename = request.POST['filename']
            from_num = int(request.POST['from_num'])
            to_num = int(request.POST['to_num'])
            pdf = PdfFileReader(file_location)
            for page in range(pdf.getNumPages()):
                newpage = from_num + page
                if newpage <= to_num:
                    name_of_split = str(int(round(time.time() * 1000)))
                    pdf_writer = PdfFileWriter()
                    pdf_writer.addPage(pdf.getPage(newpage))
                    output = f'{name_of_split}.pdf'
                    with open(new_location+output, 'wb') as output_pdf:
                        pdf_writer.write(output_pdf)
                        filelist.append(output)
                else:
                    break


            for i in filelist:
                merger.append(new_location+i)
                # os.remove(new_location+i)

            f_name = f'{file_final_name}.pdf'
            merger.write(file_dir+f_name)
            merger.close()

            feedback = {
                'status': 'success',
                'confirmed': 'success',
                'fileprocessed': f_name,
                'msg': 'Great job! Successfully extracted, kindly use filter page to edit if necessary',
                'classname': 'alert alert-primary p-1 text-center',
                }
        else:
            feedback = {
                'status': 'Failed',
                'msg': 'Invalid file uploaded or your input is out of range, please try again',
                'classname': 'alert alert-danger p-1 text-center',
            }

    except Exception as e:
        feedback = {
            'status': 'Failed',
            'msg': 'Something went wrong or input out of range, please provide valid range',
            'classname': 'alert alert-danger p-1 text-center',
        }

    return JsonResponse(feedback, safe=False)


def trim_pdf(request):
    filelist = ['1619514654043.pdf']
    text_to_search = "Fraud Detection in Health Insurance using Data Mining Techniques"
    replacement_text = "I am testing"

    pdf_file = 'frontend/src/assets/file_preprocess/1619514654099.pdf'
    docx_file = 'frontend/src/assets/extracted/sample.docx'
    newpdf_file = 'frontend/src/assets/extracted/newpdf.pdf'

    parse(pdf_file, docx_file, start=0, end=None)

    document = Document('frontend/src/assets/extracted/sample.docx')
    for paragraph in document.paragraphs:
        if text_to_search in paragraph.text:
            paragraph.text = paragraph.text.replace(text_to_search, replacement_text)

    document.save('frontend/src/assets/extracted/sample.docx')

    subprocess.check_output(['libreoffice', '--convert-to', 'pdf', docx_file])

