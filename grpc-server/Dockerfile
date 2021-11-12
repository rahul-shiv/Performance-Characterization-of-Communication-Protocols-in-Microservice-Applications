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
RUN python -m pip install -r requirements.txt
ADD . /
WORKDIR image
EXPOSE 50051 
CMD ["python","greeter_server.py"] 
