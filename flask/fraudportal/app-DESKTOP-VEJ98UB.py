import pandas as pd
from flask import Flask, render_template, request, jsonify, send_file, redirect, json
from werkzeug import secure_filename
import random
import csv as cv
import cv2
import exifread
# import numpy as np
# import matplotlib.pyplot as plt
import sys
import os, time
# import xlrd
import MySQLdb
# from textblob import TextBlob
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Ayodele1'
app.config['MYSQL_DB']='media_db'
mysql=MySQL(app)
usersecret='admin'

@app.route('/')
def index():
    return  render_template('index.html')


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
    res=cur.execute("SELECT * FROM registration WHERE matricno=%s ORDER BY SemesterID DESC", (matricno, ))
    # res=cur.execute(query, (matricno, ))
    if res > 0:
        row_headers=[x[0] for x in cur.description]
        rv = cur.fetchall()
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
    return json.dumps(message)


@app.route('/classfetch', methods=['POST'])
def classfetch():
    cur=mysql.connection.cursor()
    res=cur.execute("SELECT cname FROM category_tbl")
    if res > 0:
        data=cur.fetchall()
        cur.close()
        return jsonify(data)

@app.route('/uploadimages')
def uploadimages():
        return  render_template('uploadimages.html')

@app.route('/performance')
def performance():
        return  render_template('performance.html')


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

@app.route("/createclass")
def createclass():
    return render_template('createclass.html')

@app.route("/statistics")
def statistics():
    return render_template('statistics.html')

@app.route("/uploadcourse")
def uploadcourse():
    return render_template('uploadcourse.html')

@app.route("/uploadexamscore")
def uploadexamscore():
    return render_template('uploadexamscore.html')



@app.route("/insertclass", methods=['POST'])
def insertclass():
    if request.method=='POST':
        msg=[]
        post=request.form
        cname=post['cname']
        dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
        cur=mysql.connection.cursor()
        res=cur.execute("SELECT * FROM category_tbl WHERE cname=%s", (cname,))
        if res > 0:
            msg.append('exist')
            return jsonify(msg)
        cur.execute("INSERT INTO category_tbl(cname, status, date_Created) VALUES(%s, %s, %s)", (cname, 1, dateCreated))
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
            res=cur.execute("SELECT * FROM category_tbl ORDER BY id DESC")
        elif tablename=='totalcourse':
            res=cur.execute("SELECT * FROM registration ORDER BY MatricNo ASC")
        elif tablename=='couseupload':
            res=cur.execute("SELECT c.classid, c.id, l.cname, c.dateCreated, session, semester, c.filename FROM course_tbl c INNER JOIN category_tbl l on l.id=c.classid ORDER BY c.id DESC")
        elif tablename=='resultdata':
            res=cur.execute("SELECT c.classid, c.id, l.cname, c.dateCreated, session, semester, c.filename FROM resultfile_tbl c INNER JOIN category_tbl l on l.id=c.classid ORDER BY c.id DESC")
        elif tablename=='listimages':
            res=cur.execute("SELECT * FROM image_tbl i INNER JOIN category_tbl c on c.id=i.classid ORDER BY size ASC")
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
        tdname=post['tdname']
        cur=mysql.connection.cursor()
        if tdname=="trashlevel":
            query="DELETE FROM category_tbl WHERE id = %s"
        elif tdname=="trashcourse":
            query="DELETE FROM course_tbl WHERE id = %s"
        res=cur.execute(query, (ids, ))
        if res:
            mysql.connection.commit()
            return jsonify("deleted")
        return jsonify("failed")

@app.route('/listoption', methods=['POST'])
def listoption():
    json_data=[]
    message={
        "msg":"norecord"
    }
    if request.method=='POST':
        cur=mysql.connection.cursor()
        res=cur.execute("SELECT * FROM category_tbl ORDER BY id DESC")
        if res > 0:
            row_headers=[x[0] for x in cur.description]
            rv = cur.fetchall()
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            return json.dumps(json_data)
        return json.dumps(message)



@app.route("/counter", methods=['POST'])
def counter():
    json_data=[]
    if request.method=='POST':
        cur=mysql.connection.cursor()
        post=request.form
        ids=post['id']
        res=''
        res=cur.execute("SELECT count(distinct MatricNo) FROM result_tbl")
        if res >= 0:
            rv = cur.fetchall()
            json_data.append(rv)
            res=cur.execute("SELECT count(RegistrationID) FROM registration")
            if res >= 0:
                rv = cur.fetchall()
                json_data.append(rv)
                res=cur.execute("SELECT count(id) FROM result_tbl")
                if res >= 0:
                    rv = cur.fetchall()
                    json_data.append(rv)
        return json.dumps(json_data)



@app.route('/bulkimages', methods=['POST'])
def bulkimages():
    getfiles=request.files.getlist("filename")
    classid=request.form['cid']
    cur=mysql.connection.cursor()
    dateCreated=time.strftime('%Y-%m-%d %H:%M:%S')
    UPLOAD_FOLDER = 'static/document/uploadedfiles/'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    for file in getfiles:
        randomnum=random.randint(1, 99999)
        width=1
        vresolution=1
        hresolution=1
        dimensions=1
        size=1
        filen=str(randomnum)+file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filen))
        size = os.path.getsize('static/document/uploadedfiles/'+filen)
        with open(r'static/document/uploadedfiles/'+filen, 'rb') as f_jpg:
            tags = exifread.process_file(f_jpg, details=True)
            maker = tags['Image Make']
            camera=tags['Image Model']
            height=tags['EXIF DateTimeOriginal']
        res=cur.execute("INSERT INTO image_tbl(classid, filename, height, width, vresolution, hresolution, dimensions, size, dateCreated, camera, maker) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (classid, str(randomnum)+file.filename, height, width, vresolution, hresolution, dimensions, size, dateCreated, camera, maker))
        if res:
            mysql.connection.commit()
    return 'created'


if __name__ == "__main__":
    app.run(debug=True)