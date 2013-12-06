Docker-Data-Only-Container-Demo
===============================
My [Docker Global Hack Day][hackday] project to explore the concept of data-only Docker containers by setting up a workflow around pandoc ("a universal document converter")

See accompanying blog post for details: [Tiny Docker Pieces, Loosely Joined][tiny]

[hackday]: http://blog.docker.io/2013/11/docker-global-hack-day/
[tiny]: http://www.offermann.us/2013/12/tiny-docker-pieces-loosely-joined.html


Usage
-----
Build all Docker images:

    $ ./build-images.sh

Run example to see how multiple docker containers work together on a single data-only container:

    $ ./example.sh

License
-------
MIT license. Copyright (c) 2013 Tom Offermann.
