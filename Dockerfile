FROM python:3.5
ENV PYTHONUNBUFFERED 1

MAINTAINER victor

ADD ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

EXPOSE 8000

WORKDIR /website