FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir /aplication_web
WORKDIR /aplication_web

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip install -U pip setuptools
COPY requirements.txt /aplication_web/
RUN pip install -r /aplication_web/requirements.txt
ADD . /aplication_web/

# expose Django
EXPOSE 8000