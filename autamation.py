import sys
import os
import pymongo

from Docker import *


def initialSetup():
    docker build -t MongoDB-v5.3 .
    
    FROM Ubuntu:14.04
    RUN rm /bin/sh && ln -s /bin/bash /bin/sh

    MAINTAINER RONALD SAN DIEGO & RAJAT DIKSHIT & YASHWANT BABU

    RUN apt-get update && apt-get install -yq build-essential \
            libssl-dev \
            curl \
            git \
        npm \
            vim \
            ca-certificates \
            python \
            rsync \
            software-properties-common \
            wget \
            dos2unix \
            zlib1g-dev \
            gcc \
        make \
        g++ \
        python-software-properties \
            && apt-get clean

    RUN curl --silent --location https://deb.nodesource.com/setup_0.12 | sudo bash -
    RUN sudo apt-get install --yes nodejs

    RUN npm cache clean -f
    RUN npm install -g n
    RUN n stable

    RUN mkdir ~/npm-global
    RUN npm config set prefix '~/npm-global'
    #RUN export PATH=~/npm-global/bin:$PATH

    ENV PATH 	~/npm-global/bin:$PATH

    RUN npm install -g sails --unsafe-perm nodemon --save

    RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
    RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list
    RUN apt-get update
    RUN apt-get install mongodb-10gen

    RUN mkdir -p /data/db
    RUN mkdir -p /var/mongodb
    RUN chmod +x /usr/local/bin/start-project.sh \
	   && dos2unix /usr/local/bin/start-project.sh

    ADD beta.couchjumping /beta-cj



def mongoConfig():

    FROM ubuntu:14.04
    RUN rm /bin/sh && ln -s /bin/bash /bin/sh
    MAINTAINER Ronald San Diego & Yasvanth Babu & Rajat Dikshit

    RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
    RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list

    RUN apt-get update && apt-get install -yq build-essential \
    	curl \
        git \
        vim \
        wget \
        dos2unix \
    	tmux \
    	mongodb-org \
        && apt-get clean

from os.path import MongoDB-v5.3
for(dirname, dirs, files) in os.walk('MongoDB-Droplet'+range(1, 5)):
    for filename in files:
        if filename == 'mongod':
            for i in range(1, 5):
                RUN mkdir -p /data/db
                RUN chown `id -u` /data/db
                RUN mkdir /data/db/S1repset && mkdir /data/db/S2repset && mkdir /data/db/S3repset && mkdir /data/db/arbiter && mkdir /data/db/config1 && mkdir /data/db/config2 && mkdir /data/db/config3
                RUN mkdir /data/configdb
                ADD s+i+rep.sh /s+i+rep.sh
                ADD s+i+rep.js /s+i+rep.js

                RUN chmod a+x /s+i+rep.sh

                EXPOSE 20000 10000 10001 10002 10003
                ENTRYPOINT ["usr/bin/mongod"]

from os.path import MongoDB-v5.3
for(dirname, dirs, files) in os.walk('MongoDB-Droplet'+range(1, 5)):
    for filename in files:
        if filename == 'mongos':
            for i in range(1, 5):
                ADD shard-routerd+i+.sh /shard-routerd+i+.sh
                ADD shard-routerd+i+.js /shard-routerd+i+.js

                RUN chmod a+x /shard-routerd+i+.sh

                EXPOSE 23000 24000 25000 26000

                ENTRYPOINT ["usr/bin/mongos"]

def buildInfra():

    sh build-mongodb-d1.sh
    sh build-router.sh
    sh c-permission.sh
    sh m-build.sh
