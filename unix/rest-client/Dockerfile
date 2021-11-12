FROM python:3.7-alpine
COPY requirements.txt /
RUN pip install -r requirements.txt 
COPY . /
CMD ["time","python","test.py","1","1000","0","post"]
