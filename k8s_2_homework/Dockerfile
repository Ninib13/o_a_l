FROM python:3.7-alpine AS base

FROM base as builder
RUN mkdir /install
WORKDIR /install
RUN apk add --no-cache --virtual build-deps \
    file \ 
    make \ 
    gcc \
    musl-dev \ 
    libffi-dev
RUN pip3 install --upgrade pip
COPY requirements.txt ./
RUN pip3 install --prefix=/install -r ./requirements.txt 

FROM base
LABEL maintainer="Ninib"
LABEL version="0.3"
WORKDIR /home/app
COPY --from=builder /install /usr/local
COPY ./service/ ./service/ 
RUN pip3 freeze
EXPOSE 8000/tcp
ENTRYPOINT gunicorn service:app -b:8000 -w 1 -k eventlet 