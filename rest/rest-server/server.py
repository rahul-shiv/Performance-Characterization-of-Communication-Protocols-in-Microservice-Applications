from flask import Flask,request
import logging
import sys
import os
app = Flask(__name__)
app.logger.setLevel(logging.ERROR)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

mac = os.environ['MAC']

@app.route('/mac',methods = ['GET'])
def return_mac():
    return mac 



@app.route("/",methods = ['GET', 'POST'])
def hello():
    print(request.data)
    # print(request.headers)
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="unix://sock/test",port="5000")
    pass

