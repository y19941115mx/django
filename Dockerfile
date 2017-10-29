FROM hub.c.163.com/library/python:latest
ENV PYTHONUNBUFFERED 1

MAINTAINER victor

ADD ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

EXPOSE 8000

WORKDIR /website