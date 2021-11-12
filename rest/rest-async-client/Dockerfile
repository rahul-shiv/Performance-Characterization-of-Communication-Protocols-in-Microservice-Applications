FROM python:3.7-alpine
RUN apk add libevent-dev
RUN apk add py3-gevent 
COPY requirements.txt /
RUN pip install -r requirements.txt 
COPY . /
CMD ["time","python","client.py","post","100000","100"]
