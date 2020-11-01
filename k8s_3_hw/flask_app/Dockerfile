FROM python:3.7-alpine AS base

FROM base as builder
RUN mkdir /install /app
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
WORKDIR /app
COPY ./app/ ./app/ 
COPY run.sh .
RUN chmod +x run.sh
RUN pip3 freeze

FROM base
LABEL maintainer="Ninib"
LABEL version="0.5"
WORKDIR /home/app
COPY --from=builder /install /usr/local
COPY --from=builder /app .
EXPOSE 8080/tcp
ENTRYPOINT /home/app/run.sh