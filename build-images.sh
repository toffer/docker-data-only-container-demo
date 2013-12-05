#!/bin/sh

NAMES='pandoc data git-clone pandoc-convert http-server'

for name in $NAMES; do
    echo "** Building $name."
    docker build -t $name $name
    echo ""
done
