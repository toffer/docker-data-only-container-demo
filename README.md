Docker-Pandoc
=============
Pandoc, a universal document converter, in a Docker container.


Usage of Pandoc image
---------------------
The `pandoc` image gives you command line access to pandoc. Here's an example of using it to convert a
single markdown file.

1. Create data volume container.

        $ docker run -v /srv/code/docker-pandoc/examples:/data -name pandoc-data data true

2. Run pandoc on example markdown file, placing resulting HTML page in /data/output.

        $ docker run -volumes-from pandoc-data pandoc /data/markdown-doc.md -s -o /data/output/markdown-doc.html

3. Confirm HTML page is present in output directory.

        $ docker run -volumes-from pandoc-data busybox ls -al /data/output
