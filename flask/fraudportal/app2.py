from flask import Flask, render_template, request, jsonify, send_file
from flask import *
import random, math
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from textblob import TextBlob
app=Flask(__name__)
usersecret='admin'
rows=[]
uniqueid=[]
medicamentID1=[]
# data=[]
@app.route('/outliers')
def outliers():
    path='C:\\AppServ\\www\\classifier\\static\\document\\transaction.csv'
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
    return render_template('data.html', tables=sorts.to_html(classes='tablelist'))

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



@app.route('/')
def index():
    return  render_template('index.html')
    
@app.route('/home')
def home():
    return render_template('indexe.html', errormessage='Authentication confirmed')        

@app.route('/authentication', methods=['POST'])
def authentication():
    getvalue=request.form
    res=getvalue['adminid']
    if res == usersecret:
        return render_template('indexe.html', errormessage='Authentication confirmed')        
    return render_template('index.html', errormessage='Invalid userID')

@app.route('/', methods=['post'])
def fileupload():
    filec=request.files['filename']
    res=filec.filename
    reader3(res)
    return render_template('indexe.html', filename='Process successfully completed, data captured in a visual mode.')

@app.route('/reader')
def reader():
    filepath="C:\AppServ\www\classifier\static\document\estingdata.csv"
    x = []
    y = []
    csvfile=open(filepath,'r')
    plots = cv.reader(csvfile)
    for row in plots:
        x.append(row)
    return jsonify(x)

@app.route('/reader2')
def reader2():
    x=[]
    y=[]
    filepath="C:\AppServ\www\classifier\static\document\customerfeedback.csv"
    # csvfile=open(filepath, 'r')
    data = pd.read_csv(filepath)
    # for row in plots:
        # del row[0]
    # dataTop=data.head()
    # x.append(plots['feedback'])
    # x.pop(0)
    df=pd.DataFrame(data)
    for val in df['feedback']:
        x.append(val)
    return jsonify(x)
    # y.append(int(row[1]))
    # plt.bar(x, y, label='My sample graph', color='darkorange')
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.title('Ineteresting graph')
    # plt.legend()
    # # plt.show()
    # filename='januaryplot3.png'
    # plt.savefig('static/plots/'+filename)
    # return render_template('reader2.html', name = filename, imagepath ='static/plots/'+filename)
# def percentage(part, whole):
#     return 100*float(part)/float(whole)
@app.route('/')    
def reader3(filepath):
    positive=0
    negative=0
    neutral=0
    polarity=0
    count=0
    feedback=[]
    filepath='C:\AppServ\www\classifier\static\document\/'+filepath
    data=pd.read_csv(filepath)
    df=pd.DataFrame(data)
    for row in df['feedback']:
        feedback.append(row)
    feedback.pop(0)
    for lineoftext in feedback:
        count+=1
        analysis=TextBlob(lineoftext)
        polarity+=analysis.sentiment.polarity
        if(analysis.sentiment.polarity == 0.00):
            neutral+=1
        elif(analysis.sentiment.polarity < 0.00):
            negative+=1
        elif(analysis.sentiment.polarity > 0.00):
            positive+=1
    positive =  100*float(positive)/float(count)
    negative =  100*float(negative)/float(count)
    neutral =   100*float(neutral)/float(count)
    positive = format(positive, '.2f')
    negative = format(negative, '.2f')
    neutral = format(neutral, '.2f')
    labels=['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]', 'Negative ['+str(negative)+'%]',]
    sizes=[positive, neutral, negative]
    colors=['yellowgreen', 'gold', 'red']
    patches, texts=plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title('Sentiment analysis system\nCustomer feedback chart\n Total number of feedback: '+str(count)+'')
    plt.axis('equal')
    plt.tight_layout()
    randomnum=random.randint(1, 99999)
    filepathnew='static/plots/'+str(randomnum)+'.png'
    plt.savefig(filepathnew)
    plt.show()

if __name__ == '__main__':
   app.debug = True
   app.run()
    

    