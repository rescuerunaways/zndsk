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

import requests
from docopt import docopt

from url import get_url


def show(args):
    print_result(requests.get(*get_url(args)))


def print_result(res):
        print(res.json())


if __name__ == '__main__':
    args = docopt(__doc__)

if args['show']:
    show(args)


# def auth():
#         dmn = raw_input("domain:")
#         usr = raw_input("username(email):")
#         pswd = getpass.getpass('password:')
#         return dmn, usr, pswd
