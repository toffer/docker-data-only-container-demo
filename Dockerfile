# Dockerfile for Pandoc
# http://johnmacfarlane.net/pandoc/

FROM stackbrew/ubuntu:precise
MAINTAINER Tom Offermann <tom@offermann.us>

RUN apt-get update
RUN apt-get -y upgrade
