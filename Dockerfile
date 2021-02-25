FROM python:3.9.2
USER root

LABEL version="3.9.2"
LABEL description="discordのbot作成用"

ADD . /app
WORKDIR /app

RUN apt-get update && \
    apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja LC_ALL=ja_JP.UTF-8 \
    TZ=JST-9 \
    TERM=xterm

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r requirements.txt

CMD python -m http.server 80

VOLUME ["/data"]