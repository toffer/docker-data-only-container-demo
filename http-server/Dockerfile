# Dockerfile for Node http-server

FROM stackbrew/ubuntu:precise
MAINTAINER Tom Offermann <tom@offermann.us>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN echo "deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu precise main" >> /etc/apt/sources.list
RUN apt-get update

# Faster to add GPG key directly, rather than install python-software-properties
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C7917B12

RUN apt-get update
RUN apt-get install -y nodejs
RUN npm install http-server -g

ENTRYPOINT ["http-server"]
CMD ["--help"]
