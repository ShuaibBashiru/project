# from flask import Blueprint, render_template, request
# from flask_mysqldb import MySQL
# urls_api=Blueprint('urls_api', __name__)
# # app.config['MYSQL_HOST']='localhost'
# # app.config['MYSQL_USER']='root'
# # app.config['MYSQL_PASSWORD']='Ayodele1'
# # app.config['MYSQL_DB']='studentperformance'
# # mysql=MySQL(app)

# @urls_api.route("/createclass")
# def createclass():
#     return render_template('createclass.html')

# @urls_api.route("/createclass", methods=['POST'])
# def addclass():
#     if request.method=='POST':
#         classname=request.form['classname']
#         classlevel=request.form['classlevel']
#         return render_template('createclass.html', data2=[classname, classlevel])
#     return 'this is not accepted'

# @urls_api.route("/createclass")
# def addclass():
#     if request.method=='POST':
#         classname=request.form['classname']
#         classlevel=request.form['classlevel']
#         return render_template('createclass.html', data2=[classname, classlevel])
#     return 'this is not accepted'
