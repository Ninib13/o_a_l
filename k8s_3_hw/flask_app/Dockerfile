FROM python:3.7-alpine AS base
LABEL project_builder=true

FROM base as builder
LABEL project_builder=true
RUN mkdir /install /app
WORKDIR /install
COPY requirements.txt ./
RUN apk add --no-cache --virtual .build-deps \
    file \ 
    make \ 
    gcc \
    musl-dev \ 
    libffi-dev \ 
    && pip3 install --upgrade pip \ 
    && pip3 install --no-cache-dir --prefix=/install -r ./requirements.txt
WORKDIR /app
COPY ./app/ ./app/ 
COPY run.sh .
RUN chmod +x run.sh

FROM base
LABEL maintainer="Ninib"
LABEL version="0.5"
WORKDIR /home/app
COPY --from=builder /install /usr/local
COPY --from=builder /app .
EXPOSE 8080/tcp
ENTRYPOINT /home/app/run.sh