FROM python:3.6-slim

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV THEMEDIR=/project-root/themes/buruma

RUN apt-get update \
    && apt-get install --no-install-recommends -qy git curl bash


RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs

WORKDIR /project-root

COPY . /project-root
RUN pip install -r requirements.txt
RUN npm --prefix $THEMEDIR install $THEMEDIR
