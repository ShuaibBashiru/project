import pandas as pd
import face_recognition
from flask import Flask, render_template, request, jsonify, send_file, redirect, json
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import random
import csv as cv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
import os, time, serial
import xlrd
import dlib
import PIL.Image
from PIL import ImageFile
import MySQLdb
import cv2
# import seaborn as sns
# from textblob import TextBlob
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Ayodele1'
app.config['MYSQL_DB']='facedb'
mysql=MySQL(app)
usersecret='admin'

@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/facematch', methods=['POST'])
def facematch():
    images = os.listdir('static/document/known/')
    positive=0
    negative=0
    filename=''
    getvalue=request.form
    userid=str(getvalue['data'])
    # load your image
    image_to_be_matched = face_recognition.load_image_file('static/document/unknown/{}'.format(userid))
    # encoded the loaded image into a feature vector
    image_to_be_matched_encoded = face_recognition.face_encodings(
        image_to_be_matched)[0]
    # iterate over each image
    for image in images:
        # load the image
        current_image = face_recognition.load_image_file("static/document/known/" + image)
        # encode the loaded image into a feature vector
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
        # match your image with the image and check if it matches
        result = face_recognition.compare_faces(
            [image_to_be_matched_encoded], current_image_encoded, tolerance=0.30)
        # check if it was a match
        if result[0] == True:
            positive+=1
            filename=image
        else:
            negative+=1
    message={
    'positive':positive,
    'negative':negative,
    'filename':filename
    }
    return json.dumps(message)


@app.route('/startcamera', methods=['POST'])
def startcamera():
    cam = cv2.VideoCapture(1)
    cv2.namedWindow("FACE CAPTURE PANEL")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("FACE CAPTURE PANEL", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k%256 == 27:
        # ESC pressed
            cam.release()
            cv2.destroyAllWindows()
            # redirect("/dashboard", code=302)
            break
        elif k%256 == 32:
            getvalue=request.form
            userid=str(getvalue['data'])
        # SPACE pressed
            # randomnum=random.randint(1, 99999)
            newuserid=userid.replace('/', '')
            img_name = "{}.png".format(newuserid)
            cv2.imwrite('static/document/known/'+img_name, frame)
            print("{} written!".format(img_name))
            img_counter+1
            cam.release()
            cv2.destroyAllWindows()
            message={
                "msg":"created",
                "filename":img_name
            }
            return json.dumps(message)
    cam.release()
    cv2.destroyAllWindows()


@app.route('/startcameraaccess', methods=['POST'])
def startcameraaccess():
    cam = cv2.VideoCapture(1)
    cv2.namedWindow("FACE CAPTURE PANEL")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("FACE CAPTURE PANEL", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k%256 == 27:
        # ESC pressed
            cam.release()
            cv2.destroyAllWindows()
            # redirect("/dashboard", code=302)
            break
        elif k%256 == 32:
        # SPACE pressed
            newuserid='newface'
            img_name = "{}.png".format(newuserid)
            cv2.imwrite('static/document/unknown/'+img_name, frame)
            print("{} written!".format(img_name))
            cam.release()
            cv2.destroyAllWindows()
            message={
                "msg":"created",
                "filename":img_name
            }
            return json.dumps(message)
    cam.release()
    cv2.destroyAllWindows()


@app.route('/inserttiming', methods=['POST'])
def inserttiming():
    getvalue=request.form
    userid=getvalue['userid']
    dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
    timeout=time.strftime('%Y-%m-%d %H:%M:%S')
    timein=time.strftime('%Y-%m-%d %H:%M:%S')
    counter=1
    cur=mysql.connection.cursor()
    res=cur.execute("SELECT userid FROM accesscontrol WHERE userid=%s", (userid,))
    if res > 0:
        res=cur.execute("UPDATE accesscontrol SET timeout=%s, counter=%s, dateCreated=%s WHERE userid=%s", (timeout, counter, dateCreated, userid))
        if res:
            mysql.connection.commit()
            enabledev()
            return 'created'
    else:
        res=cur.execute("INSERT INTO accesscontrol(userid, timein, counter, dateCreated) VALUES(%s, %s, %s, %s)", (userid, timein, counter, dateCreated))
        if res:
            mysql.connection.commit()
            enabledev()
            return 'created'

    cur.close()

def enabledev():
    ser = serial.Serial('COM8', 9600)
    time.sleep(2)
    ser.write('open'.encode())
    time.sleep(0.5)
    ser.close()

@app.route('/sampledata')
def sampledata():
    data=pd.read_csv('static/document/uploadedfiles/sample.csv')
    data=pd.DataFrame(data)
    return data.to_html()

@app.route('/checkperformance', methods=['POST'])
def checkperformance():
    json_data=[]
    message={
        "msg":"norecord"
    }
    getvalue=request.form
    matricno=getvalue['matricno']
    cur=mysql.connection.cursor()
    res=cur.execute("SELECT * FROM result_tbl WHERE matricno=%s", (matricno, ))
    # res=cur.execute(query, (matricno, ))
    if res > 0:
        row_headers=[x[0] for x in cur.description]
        rv = cur.fetchall()
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
    return json.dumps(message)
    #     return  render_template('checkresult.html', result='No records found')
    # data=cur.fetchall()[0]
    # cur.close()
    # path='static/document/uploadedfiles/'+data[0]
    # getfile=pd.read_csv(path, delimiter=',')
    # res=getfile
    # sort=res[res['matricno'].str.match(matricno)]
    # sort['percentage%']=(sort['test']*0.4)+(sort['exam']*0.6)
    # sort.drop(sort.filter(regex="Unname"),axis=1, inplace=True)
    # return render_template('checkresult.html', result=sort.to_html(classes='itemlist'))

@app.route('/classfetch', methods=['POST'])
def classfetch():
    cur=mysql.connection.cursor()
    res=cur.execute("SELECT levelname FROM category")
    if res > 0:
        data=cur.fetchall()
        cur.close()
        return jsonify(data)

@app.route('/uploadresult')
def uploadresult():
        return  render_template('uploadresult.html')


@app.route('/performance')
def performance():
        return  render_template('performance.html')

# @app.route('/checkresult')
# def checkresult():
#     cur=mysql.connection.cursor()
#     res=cur.execute("SELECT * FROM __level")
#     if res > 0:
#         data=cur.fetchall()
#         cur.close()
#     return  render_template('checkresult.html', classlist=data)

# @app.route('/uploadclass')
# def uploadclass():
#     cur=mysql.connection.cursor()
#     res=cur.execute("SELECT * FROM __level")
#     if res > 0:
#         data=cur.fetchall()
#         cur.close()
#         return render_template('uploadclass.html', classlist=data)

@app.route('/uploadfile', methods=['POST'])
def uploadfile():
    getvalue=request.form
    classid=getvalue['cid']
    session=getvalue['session']
    semester=getvalue['semester']
    getfile=request.files['filename']
    filename=getfile.filename
    dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
    cur=mysql.connection.cursor()
    res=cur.execute("SELECT * FROM course_tbl WHERE classid=%s and session=%s and semester=%s", (classid, session, semester))
    if res > 0:
        return 'exist'
    randomnum=random.randint(1, 99999)
    getfile.save(os.path.join('static/document/uploadedfiles/', str(randomnum)+filename))
    filepath='static/document/uploadedfiles/'+str(randomnum)+filename
    res=cur.execute("INSERT INTO course_tbl(classid, session, semester, filename, dateCreated) VALUES(%s, %s, %s, %s, %s)", (classid, session, semester,  str(randomnum)+filename, dateCreated))
    if res:
       fileuploader(filepath)
       return 'created'


# @app.route('/fileuploader')
def fileuploader(file_name):
    cur=mysql.connection.cursor()
    book=xlrd.open_workbook(file_name)
    sheet=book.sheet_by_name('Sheet3')
    query="""INSERT INTO registration(SessionID, SemesterID, CourseCode, Courseid, ContinuosAssesment, Exam,
    Score, Grade, CourseUnit, ProgrammeID, LevelID, MatricNo, CPoint, SemID, DateCreated, TimeCreated,
    AStatus, ProgrammeTypeID, ProgrammeID2, DeptId)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    for r in range(1, sheet.nrows):
        SessionID=sheet.cell(r, 0).value
        SemesterID=sheet.cell(r, 1).value
        CourseCode=sheet.cell(r, 2).value
        Courseid=sheet.cell(r, 3).value
        ContinuosAssesment=sheet.cell(r, 4).value
        Exam=sheet.cell(r, 5).value
        Score=sheet.cell(r, 6).value
        Grade=sheet.cell(r, 7).value
        CourseUnit=sheet.cell(r, 8).value
        ProgrammeID=sheet.cell(r, 9).value
        LevelID=sheet.cell(r, 10).value
        MatricNo=sheet.cell(r, 11).value
        CPoint=sheet.cell(r, 12).value
        SemID=sheet.cell(r, 13).value
        DateCreated=sheet.cell(r, 14).value
        TimeCreated=sheet.cell(r, 15).value
        AStatus=sheet.cell(r, 16).value
        ProgrammeTypeID=sheet.cell(r, 17).value
        ProgrammeID2=sheet.cell(r, 18).value
        DeptId=sheet.cell(r, 19).value
        values = (SessionID, SemesterID, CourseCode, Courseid,ContinuosAssesment,
        Exam, Score, Grade, CourseUnit, ProgrammeID, LevelID, MatricNo, CPoint,
        SemID, DateCreated, TimeCreated, AStatus, ProgrammeTypeID, ProgrammeID2, DeptId)
        cur.execute(query, values)
    cur.close()
    mysql.connection.commit()

# upload result file here
@app.route('/uploadresfile', methods=['POST'])
def uploadresfile():
    getvalue=request.form
    classid=getvalue['classnameid']
    getfile=request.files['filename']
    filename=getfile.filename
    dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
    cur=mysql.connection.cursor()
    randomnum=random.randint(1, 99999)
    getfile.save(os.path.join('static/document/uploadedfiles/', str(randomnum)+filename))
    filepath='static/document/uploadedfiles/'+str(randomnum)+filename
    res=cur.execute("INSERT INTO resultfile_tbl(classid, filename, dateCreated) VALUES(%s, %s, %s)", (classid,  str(randomnum)+filename, dateCreated))
    if res:
       fileuploaderforres(filepath, classid)
       return 'created'


def fileuploaderforres(file_name, classid):
    cur=mysql.connection.cursor()
    book=xlrd.open_workbook(file_name)
    sheet=book.sheet_by_name('Sheet1')
    dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
    query="""INSERT INTO result_tbl(cid, name, matric, gender, dateCreated)
    VALUES(%s, %s, %s, %s, %s)"""
    for r in range(1, sheet.nrows):
        name=sheet.cell(r, 1).value
        matric=sheet.cell(r, 2).value
        gender=sheet.cell(r, 3).value
        values = (classid, name, matric, gender, dateCreated)
        cur.execute(query, values)
    cur.close()
    mysql.connection.commit()

@app.route('/dashboard')
def dashboard():
    return render_template('indexe.html')

@app.route('/authentication', methods=['POST', 'GET'])
def authentication():
    getvalue=request.form
    res=getvalue['adminid']
    if res == usersecret:
        return redirect("/dashboard", code=302)
    return render_template('index.html', errormessage='Invalid userID')

@app.route('/uploader', methods=['post'])
def fileupload():
    if request.method=='post':
        f=request.files['filename']
        filenm=f.filename
        f.save(os.path.join('static/document/uploadedfiles', secure_filename(filenm)))
        return 'successfully uploaded'
    return 'this is not a post method'


@app.route("/uploadcourse")
def uploadcourse():
    return render_template('uploadcourse.html')

@app.route("/insertclass", methods=['POST'])
def insertclass():
    if request.method=='POST':
        msg=[]
        post=request.form
        levelname=post['levelname']
        dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
        cur=mysql.connection.cursor()
        res=cur.execute("SELECT * FROM level WHERE levelname=%s", (levelname,))
        if res > 0:
            msg.append('exist')
            return jsonify(msg)
        cur.execute("INSERT INTO level(levelname, status, dateCreated) VALUES(%s, %s, %s)", (levelname, 1, dateCreated))
        mysql.connection.commit()
        msg.append('created')
        return jsonify(msg)


@app.route("/createserv", methods=['POST'])
def createserv():
    if request.method=='POST':
        msg=[]
        post=request.form
        userid=post['userid']
        payid=post['payid']
        did=post['description']
        priceset=post['priceset']
        qty=post['qty']
        status='suspicious'
        CreatedBy='Admin'
        total=float(priceset)*int(qty)
        dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
        cur=mysql.connection.cursor()
        res=cur.execute("SELECT * FROM result_tbl WHERE %s BETWEEN price1 AND price2 and id= %s", (priceset, did))
        if res > 0:
            status='accurate'
        cur.execute("INSERT INTO transactions(userid,priceset,qty,payid,did,total,status,dateCreated,CreatedBy) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (userid,priceset,qty,payid,did,total,status,dateCreated,CreatedBy))
        mysql.connection.commit()
        msg.append('created')
        return jsonify(msg)

@app.route("/listdata", methods=['POST'])
def listdata():
    json_data=[]
    if request.method=='POST':
        cur=mysql.connection.cursor()
        post=request.form
        tablename=post['tablename']
        ids=post['id']
        res=''
        if tablename=='leveldata':
            res=cur.execute("SELECT * FROM level ORDER BY id DESC")
        elif tablename=='couseupload':
            res=cur.execute("SELECT c.classid, c.id, l.levelname, c.dateCreated, c.filename FROM course_tbl c INNER JOIN level l on l.id=c.classid ORDER BY c.id DESC")
        elif tablename=='resultdata':
            res=cur.execute("SELECT r.id, r.matric, r.name, r.gender, l.levelname, r.dateCreated FROM result_tbl r INNER JOIN level l on l.id=r.cid ORDER BY r.id DESC")
        elif tablename=='listtiming':
            res=cur.execute("SELECT r.id, r.matric, r.uid, r.name, r.gender, l.timein, l.timeout, l.dateCreated FROM result_tbl r INNER JOIN accesscontrol l on l.userid=r.uid ORDER BY l.dateCreated DESC")
        elif tablename=='viewdata':
            res=cur.execute("SELECT c.id, c.price2, c.price1, l.levelname, c.text, c.dateCreated FROM result_tbl c INNER JOIN level l on l.id=c.cid WHERE c.cid=%s", (ids, ))
        elif tablename=='userlist':
            res=cur.execute("SELECT * FROM profile ORDER BY id ASC")
        elif tablename=='viewuser':
            res=cur.execute("SELECT * FROM profile ORDER BY id ASC")
        elif tablename=='userprofile':
            res=cur.execute("SELECT * FROM profile WHERE email=%s", (ids, ))
        elif tablename=='listcurrentpayservice':
            res=cur.execute("SELECT r.text, t.id, t.priceset, t.dateCreated, qty, payid, did, total FROM transactions t INNER JOIN result_tbl r on r.id=t.did WHERE payid=%s", (ids, ))
        elif tablename=='listpaymenttopay':
            res=cur.execute("SELECT r.text, p.filename, p.surname, p.oname, t.id, t.priceset, t.dateCreated, qty, payid, did, total FROM transactions t INNER JOIN result_tbl r on r.id=t.did INNER JOIN profile p on p.id=t.userid WHERE t.status=%s and payid=%s", ('accurate', ids))
        elif tablename=='flaggedlist2':
            res=cur.execute("SELECT r.text, p.filename, p.surname, p.oname, t.id, r.price1, r.price2, t.priceset, t.createdBy, t.dateCreated, qty, payid, did, total FROM transactions t INNER JOIN result_tbl r on r.id=t.did INNER JOIN profile p on p.id=t.userid WHERE t.status=%s", ('suspicious', ))
        if res > 0:
            row_headers=[x[0] for x in cur.description]
            rv = cur.fetchall()
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)

@app.route("/trash", methods=['POST'])
def trash():
    if request.method=='POST':
        msg=[]
        query=''
        post=request.form
        ids=post['id']
        tdname=post['tablename']
        message1={
            'msg':'deleted'
        }
        message2={
            'msg':'error'
        }
        cur=mysql.connection.cursor()
        if tdname=="trashlevel":
            query="DELETE FROM level WHERE id = %s"
        elif tdname=="trashaccount":
            query="DELETE FROM result_tbl WHERE id = %s"
        elif tdname=="user":
            query="DELETE FROM profile WHERE id = %s"
        elif tdname=="trashcurrentservice":
            query="DELETE FROM transactions WHERE id = %s"
        res=cur.execute(query, (ids, ))
        if res:
            mysql.connection.commit()
            return json.dumps(message1)
        return json.dumps(message2)

@app.route('/listoption', methods=['POST'])
def listoption():
    json_data=[]
    message={
        "msg":"norecord"
    }
    if request.method=='POST':
        cur=mysql.connection.cursor()
        res=cur.execute("SELECT * FROM level ORDER BY id DESC")
        if res > 0:
            row_headers=[x[0] for x in cur.description]
            rv = cur.fetchall()
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            return json.dumps(json_data)
        return json.dumps(message)

@app.route('/listoption2', methods=['POST'])
def listoption2():
    json_data=[]
    message={
        "msg":"norecord"
    }
    if request.method=='POST':
        post=request.form
        ids=post['id']
        cur=mysql.connection.cursor()
        res=cur.execute("SELECT id, text FROM result_tbl WHERE cid =%s ORDER BY text asc", (ids, ))
        if res > 0:
            row_headers=[x[0] for x in cur.description]
            rv = cur.fetchall()
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            return json.dumps(json_data)
        return json.dumps(message)

@app.route('/analysis', methods=['POST'])
def analysis():
    positive=0
    negative=0
    neutral=0
    polarity=0
    count=0
    feedback=[]
    post=request.form
    ids=post['data']
    cur=mysql.connection.cursor()
    res=cur.execute("SELECT * FROM result_tbl WHERE cid=%s", (ids,))
    res=cur.fetchall()
    df=pd.DataFrame(res)
    for row in df[2]:
        feedback.append(row)
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
    labels=['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]', 'Negative ['+str(negative)+'%]']
    sizes=[positive, neutral, negative]
    colors=['yellowgreen', 'gold', 'red']
    patches, texts=plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.title('Sentiment analysis system\nCustomer feedback chart\n Total number of feedback: '+str(count)+'')
    plt.axis('equal')
    plt.tight_layout()
    randomnum=random.randint(1, 99999)
    newfilename=str(randomnum)+'.png'
    dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
    filepathnew='static/plots/'+str(randomnum)+'.png'
    cur.execute("INSERT INTO report_tbl(filename, dateCreated) VALUES(%s, %s)", (newfilename, dateCreated))
    mysql.connection.commit()
    cur.close()
    plt.savefig(filepathnew)
    plt.show()
    return 'created'

@app.route("/account")
def account():
    return render_template('account.html')

@app.route("/insertaccount", methods=['POST'])
def insertpatient():
    if request.method=='POST':
        post=request.form
        userid=post['matricno']
        dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
        status=1
        message={
            "msg":"created"
        }
        exist={
            "msg":"exist"
        }
        randomnum=random.randint(1, 99999)
        skey=random.randint(1, 99999)
        cur=mysql.connection.cursor()
        res=cur.execute("SELECT * FROM userfaces WHERE email=%s", (email,))
        if res > 0:
            return json.dumps(exist)
        cur.execute("INSERT INTO userfaces(userid, dateCreated, createdBy) VALUES(%s, %s, %s)", (userid, oname, dateCreated))
        mysql.connection.commit()
        return json.dumps(message)


@app.route("/createclass?levelname=")
def createclass():
    return render_template('createclass.html')

@app.route("/recordlist")
def recordlist():
    return render_template('recordlist.html')

@app.route("/createservice")
def createservice():
    return render_template('createservice.html')

@app.route("/makepayment")
def makepayment():
    return render_template('makepayment.html')

@app.route("/flagged")
def flagged():
    return render_template('flaggedlist.html')

if __name__ == "__main__":
    app.run(debug=True)