#!/usr/bin/env python

"""Convert Directory.

Usage: convert_directory.py <src_dir> <dest_dir>

-h --help    show this
"""


import errno
import os
import subprocess

from docopt import docopt


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def convert_directory(src, dest):
    mkdir_p(dest)

    # Convert the files in place
    for root, dirs, files in os.walk(src):
        for filename in files:
            if filename.endswith(('md', 'markdown')):
                name, ext = filename.split('.')
                html_filename = '.'.join([name, 'html'])
                md_path = os.path.join(root, filename)
                html_path = os.path.join(root, html_filename)
                subprocess.call(['pandoc', md_path, '-s', '-o', html_path])

    # Rsync just the html files to dest
    subprocess.call(['rsync', '-av', '--include=*.html', '--filter=-! */',
                     '--remove-source-files', src + '/', dest])

def main():
    pass

if __name__ == '__main__':
    args = docopt(__doc__, version='Convert Directory 0.1')
    src = args['<src_dir>']
    dest = args['<dest_dir>']

    convert_directory(src, dest)
