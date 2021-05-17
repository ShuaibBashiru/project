import pandas as pd
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import random
import csv as cv
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from routes import *
app = Flask(__name__)
# app.register_blueprint(urls_api)
usersecret='1234'
username='admin'
@app.route('/')
def index():
    return  render_template('index.html')    

@app.route('/authentication', methods=['POST'])
def authentication():
    getvalue=request.form
    adminid=getvalue['adminid']
    user=getvalue['username']
    if str(adminid) == str(usersecret) and str(user)==str(username):
        return render_template('indexe.html', errormessage='Authentication confirmed')        
    return render_template('index.html', errormessage='Invalid userID')

@app.route('/uploader', methods=['post'])
def fileupload():
    if request.method=='post':

        f=request.files['filename']
        filenm=f.filename
        f.save(os.path.join('static/document/uploadedfiles', secure_filename(filenm)))
        return 'successfully uploaded'
    return 'this is not a post method'

rows=[]
uniqueid=[]
medicamentID1=[]
getids=[]
# data=[]
@app.route('/outliers', methods=['post'])
def outliers():
    path='C:\\pythonproject\\fraudportal\\static\\document\\transaction.csv'
    df = pd.read_csv(path, delimiter=',')
    df=pd.DataFrame(df, columns=['medicamentID', 'symptoms', 'amount'])
    # uniqueid=df['symptoms'].unique()
    df['v1'] = df.groupby('medicamentID')['symptoms'].transform('size')
    # df['Amount'] = df.groupby('medicamentID')['amount'].transform('sum')
    df['v2'] = df.groupby(['medicamentID', 'amount'])['amount'].transform('size')
    groups=df.groupby('medicamentID').sum().fillna(0)
    groups['classficationStatus']=groups['v1']/groups['v2']
    # groups['result']=groups['v1']/groups['v2']
    sorts=groups.sort_values(['classficationStatus'], ascending=False)
    sorts.loc[sorts.classficationStatus != 1.000000, 'classficationStatus'] = 'Suspicious'
    sorts.loc[sorts.classficationStatus == 1.000000, 'classficationStatus'] = 'Accurate'
    sorts2=sorts.loc[sorts.classficationStatus=='Suspicious']
    getids=df['medicamentID'].unique()
    return render_template('indexe.html', id=getids, tables=sorts.to_html(classes='tablelist'), tables2=sorts2.to_html(classes='tablelist'))

    # sorts.style.apply('red')
    # left = [1, 2, 3, 4, 5] 
    # for line in sorts['result']:
    #     data.append(line)
    # height = data 
    # tick_label = df['symptoms'].unique()
    # plt.bar(left, height, tick_label = tick_label, 
	# width = 0.8, color = ['red', 'green']) 
    # plt.xlabel('x - axis') 
    # plt.ylabel('y - axis') 
    # # plot title 
    # plt.title(data) 
    # randomnum=random.randint(1, 99999)
    # filepathnew='static/plots/'+str(randomnum)+'.png'
    # plt.savefig(filepathnew)


@app.route('/fetchbyid', methods=['POST'])
def fetchbyid():
    getvalue=request.form
    res=getvalue['ids']
    path='C:\\pythonproject\\fraudportal\\static\\document\\transaction.csv'
    df = pd.read_csv(path, delimiter=',')
    df=pd.DataFrame(df, columns=['medicamentID', 'symptoms', 'amount'])
    getids=df['medicamentID'].unique()
    df=df.groupby('medicamentID').get_group(int(res))
    return render_template('indexe.html', id=getids, tables=df.to_html(classes='tablelist'))

if __name__ == "__main__":
    app.run()