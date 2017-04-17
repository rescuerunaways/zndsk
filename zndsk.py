#! /usr/bin/python

"""Zendesk tickets viewer.

Usage:
  zndsk.py show [--page=<page>]
  zndsk.py show <ticket>
  zndsk.py (-h | --help)

Options:
  -h --help            Show this help screen.
  --page=<number>      Show tickets page.
"""

from docopt import docopt

from controller import get


def show(args):
    print(get(args).text)

if __name__ == '__main__':
    args = docopt(__doc__)

if args['show']:
    show(args)

