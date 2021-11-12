FROM python:3.7-alpine as base

RUN apk add --update --no-cache \
    gcc \
    linux-headers \
    make \
    musl-dev \
    python-dev \
    g++
ENV GRPC_PYTHON_VERSION 1.15.0
COPY requirements.txt /
RUN pip install -r requirements.txt
ADD . /
WORKDIR image
CMD ["time","python","greeter_client.py","1","1000","0"]
