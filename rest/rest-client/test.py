import sys
#import requests
#import requests_unixsocket as requests
import fast_requests as s
import base64

method = sys.argv[4]
count = int(sys.argv[1])
par = sys.argv[2]

if sys.argv[3]=="0":
    PATH = "http://172.17.0.2:5000/"
elif sys.argv[3]=="1":
    PATH = "http://127.0.0.1:5000/"
elif sys.argv[3]=="2":
    PATH = "http+unix://%2Fhome%2Frshiv%2FDocuments%2Fresearch%2Fdocker%2Frest%2Frest-server%2Ftest/"
if par=="none":
	encoded_string = b'abcd'
else:
	with open(par+"k.jpeg","rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())
#s = requests.Session()
print(sys.getsizeof(encoded_string))
while(count):
    message = {'message': 'Hello World'}
    if method == 'get':
        requests.get(PATH,params = message)
    elif method == 'post':
        print(s.post(PATH,data = encoded_string+str(count).encode()).text)
    count-=1
