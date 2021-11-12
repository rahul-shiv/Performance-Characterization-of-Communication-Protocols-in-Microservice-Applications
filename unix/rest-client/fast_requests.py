import requests
import requests_unixsocket
import re
import os
mac = os.environ['MAC']
mapped_ips ={}

def get(*args,**kwargs):
    address = args[0]
    pattern = re.compile('.*\/\/[^\/]*\/')
    address = re.match(pattern,address)[0]
    if address not in mapped_ips:
        response = requests.get(address+'mac')
        mapped_ips[address] = response.text==mac
    if mapped_ips[address]:
        return requests_unixsocket.get('http+unix://%2Fsock%2Ftest/',*args[1:],**kwargs)
    else:
        return requests.get(*args,**kwargs)

def post(*args,**kwargs):
    address = args[0]
    pattern = re.compile('.*\/\/[^\/]*\/')
    address = re.match(pattern,address)[0]
    if address not in mapped_ips:
        response = requests.get(address+'mac')
        print(response,mac)
        mapped_ips[address] = response.text==mac
    if mapped_ips[address]:
        print(1,'http+unix://%2Fsock%2Ftest/',*args[1:])
        return requests_unixsocket.post('http+unix://%2Fsock%2Ftest/',*args[1:],**kwargs)
    else:
        return requests.post(*args,**kwargs)

