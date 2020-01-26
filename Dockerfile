FROM python:3.7-slim-buster

ARG app_name="beers_api"
ENV APP_NAME $beers_api

ARG pipenv_dev=0
ENV PIPENV_DEV $pipenv_dev
ARG pipenv_cache_dir=/tmp/.pipenv_cachedir
ENV PIPENV_CACHE_DIR $pipenv_cache_dir

ARG DOCKERIZE_VERSION="v0.6.1"

ENV PYTHONUNBUFFERED 1

ENV DEBIAN_FRONTEND noninteractive
ENV LANGUAGE es_ES.UTF-8
ENV LANG es_ES.UTF-8
ENV LC_ALL es_ES.UTF-8
ENV LC_CTYPE es_ES.UTF-8

ENV PIPENV_PIPFILE /tmp/Pipfile

RUN apt-get update && apt-get install -y --no-install-recommends \
  locales gettext wget libmariadb-dev-compat build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

ENV TZ Europe/Madrid
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

RUN echo "es_ES.UTF-8 UTF-8" > /etc/locale.gen && dpkg-reconfigure locales

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN mkdir -p $PIPENV_CACHE_DIR

RUN pip install pipenv

COPY ./beers_api /code

COPY ./Pipfile $PIPENV_PIPFILE

RUN pipenv lock && pipenv sync

RUN apt-get purge -y libmariadb-dev-compat build-essential