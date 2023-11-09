# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.9-alpine AS builder
EXPOSE 8000
COPY web_radius /app
WORKDIR /app

# RUN apt install dos2unix
# RUN dos2unix requirements.txt

RUN pip install --upgrade pip
#RUN apk add build-base openldap-dev python2-dev python3-dev
#RUN pip install django-auth-ldap

COPY web_radius/requirements.txt /app
RUN pip3 install -r requirements.txt

# default timezone
ENV TZ Europe/Moscow


ENV DB_HOST=10.100.9.188
ENV DB_PORT=6543
ENV DB_USER=radius
ENV DB_PASS=radpass
ENV DB_NAME=radius

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
