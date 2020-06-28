FROM python:3.6-alpine
MAINTAINER Affan Muddassir

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip install -r /requirements.txt

RUN mkdir /djangonautic
WORKDIR /djangonautic
COPY ./djangonautic /djangonautic

RUN adduser -D user
USER user