#!/usr/bin/env python

"""Git Clone Docs

Usage: git-clone-docs.py <repository>

-h --help    show this
"""


import errno
import os
import subprocess
import sys

from docopt import docopt


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def clone(repo, dst='/data/tmp'):
    subprocess.call(['git', 'clone', repo, dst])

def has_markdown(path):
    """Make sure markdown files exist in doc_path."""
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(('.md', '.markdown')):
                return True
    return False

def find_docs(repo_dir):
    """Find doc directory in repo directory.

    If a sub-directory named 'doc' or 'docs' is found, assume
    that's the correct directory with docs. Otherwise, use the 
    root directory.

    The doc directory must contain at least one markdown file.

    """
    # Default path to docs is root directory
    doc_path = repo_dir

    # Check for 'doc' or 'docs' directory
    os.chdir(repo_dir)
    entries = os.listdir(repo_dir)
    for entry in entries:
        path = os.path.abspath(entry)
        if os.path.isdir(path) and entry in ['doc', 'docs']:
            doc_path = path

    if has_markdown(doc_path):
        return doc_path
    else:
        return None

def main(repo):
    repo_path = '/data/tmp'
    mkdir_p(repo_path)
    clone(repo, repo_path)
    doc_path = find_docs(repo_path)
    
    if doc_path:
        os.rename(doc_path, '/data/md')
        sys.exit(0)
    else:
        print "No docs directory found."
        sys.exit(1)


if __name__ == '__main__':
    args = docopt(__doc__, version='git-clone-docs 0.1')
    repo = args['<repository>']

    main(repo)

