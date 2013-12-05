# Dockerfile for pandoc-doc-builder
# Convert a directory of markdown files to directory of html files.

FROM pandoc
MAINTAINER Tom Offermann <tom@offermann.us>

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list

RUN apt-get update
RUN apt-get -y install rsync python python-pip

RUN pip install --upgrade pip
RUN pip install docopt

ADD convert-directory.py /convert-directory.py
RUN chmod 755 /convert-directory.py

ENTRYPOINT ["/convert-directory.py"]
CMD ["-h"]
