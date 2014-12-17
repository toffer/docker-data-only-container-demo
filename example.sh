#!/bin/sh
# Example script to show how all the pieces fit together.

set -e

echo "** Creating data container."
docker run --name pandoc-data data true

echo "** Cloning git repository to data container and saving doc directory."
docker run --volumes-from pandoc-data git-clone https://github.com/isaacs/npm

echo "** Converting doc directory to html using pandoc."
docker run --volumes-from pandoc-data pandoc-convert /data/md /data/html

echo "** Listing /data/html on data container to show resulting HTML files."
docker run --volumes-from pandoc-data busybox ls -al /data/html

echo "** Serving /data/html on port 8080."
docker run -d --volumes-from pandoc-data -p 8080:8080 http-server /data/html
