import sys
from grequests import async
import base64
PATH = "http://172.17.0.2:5000/"

method = sys.argv[1]
count = int(sys.argv[2])
par = sys.argv[3]

if par=="none":
	encoded_string = b'abcd'
else:
	with open(par+"k.jpeg","rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())
print(sys.getsizeof(encoded_string))
async_list = list()
while(count):
    message = {'message': 'Hello World'}
    if method == 'post':
        reply = async.post(PATH,data = encoded_string+str(count).encode())
        async_list.append(reply)
    count-=1
async.map(async_list)
