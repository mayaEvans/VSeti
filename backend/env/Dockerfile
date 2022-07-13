FROM python:3.10.2

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y lsb-release

COPY . /srv/html/djangoTask
WORKDIR /srv/html/djangoTask
RUN pip install -r /srv/html/djangoTask/env/requirements.txt
