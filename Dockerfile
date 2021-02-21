FROM python:3.9.2
USER root

LABEL version="3.9.2"
LABEL description="discordのbot作成用"

ADD . /app
WORKDIR /app

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja LC_ALL=ja_JP.UTF-8
ENV TZ=JST-9
ENV TERM=xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

CMD python -m http.server 80

VOLUME ["/data"]