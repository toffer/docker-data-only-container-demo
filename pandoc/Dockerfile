# Dockerfile for Pandoc
# http://johnmacfarlane.net/pandoc/

FROM stackbrew/ubuntu:precise
MAINTAINER Tom Offermann <tom@offermann.us>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list

RUN apt-get update
RUN apt-get -y install pandoc

ENTRYPOINT ["/usr/bin/pandoc"]
CMD ["--help"]
