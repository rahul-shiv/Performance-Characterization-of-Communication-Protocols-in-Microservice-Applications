import sys
sys.path.append('./gen-py')
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import base64
import sys
import logging 
from image import Service
from image.ttypes import Image
import base64

encoded_string = b"abcd"
if sys.argv[3]=="0":
    host = '172.17.0.2'
elif sys.argv[3]=="1":
    host = '127.0.0.1'
port = 9090
count = int(sys.argv[1])
data = sys.argv[2]

if data=="none":
    encoded_string  = b'abcd'
else:
    with open(data+"k.jpeg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
message = Image()
message.blob = encoded_string

print(sys.getsizeof(encoded_string))

socket = TSocket.TSocket(host, port)
transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = Service.Client(protocol)
transport.open()

# binary_data = base64.b64encode(data.encode('utf-8'))
# print(binary_data)
while count:

    response = client.send(message)
    # print(count,file=sys.stderr)
    
    count-=1
transport.close()
