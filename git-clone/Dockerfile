# Dockerfile for git-clone-docs
# Clone a git repository, find the directory of doc files in Markdown,
# and save the doc directory to /data/src.

FROM stackbrew/ubuntu:precise
MAINTAINER Tom Offermann <tom@offermann.us>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list

RUN apt-get update
RUN apt-get -y install git python python-pip
RUN pip install --upgrade pip docopt

VOLUME /data

ADD git-clone-docs.py /git-clone-docs.py
RUN chmod 755 /git-clone-docs.py

ENTRYPOINT ["/git-clone-docs.py"]
CMD ["-h"]
