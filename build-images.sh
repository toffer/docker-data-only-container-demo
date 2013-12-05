#!/bin/sh

echo "** Building pandoc"
cd pandoc
docker build -t pandoc .

echo "** Building data"
cd ../data
docker build -t data .

echo "** Building git-clone"
cd ../git-clone
docker build -t git-clone .

echo "** Building pandoc-convert"
cd ../pandoc-convert
docker build -t pandoc-convert .

echo "** Building http-server"
cd ../http-server
docker build -t http-server .
