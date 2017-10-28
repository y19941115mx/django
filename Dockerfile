FROM hub.c.163.com/library/python:3
ENV PYTHONUNBUFFERED 1

MAINTAINER victor

ADD ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

EXPOSE 8000

WORKDIR /website