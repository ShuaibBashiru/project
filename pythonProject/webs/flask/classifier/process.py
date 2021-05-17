
@app.route('/process', methods=['GET'])
def process():
    getvalue=request.form
    myname2=getvalue['myname']
    return myname2

