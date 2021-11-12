FROM python:3.7-alpine as base
COPY requirements.txt /
RUN pip install -r requirements.txt
ADD . /
WORKDIR image
EXPOSE 9090
CMD ["time","python","client.py","1","1000","0"]
