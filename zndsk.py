#! /usr/bin/python

"""Zendesk tickets viewer.

Usage:
  zndsk.py show [--page=<ticket>]
  zndsk.py show <ticket>
  zndsk.py (-h | --help)

Options:
  -h --help            Show this help screen.
  --page=<number>      Show tickets page.
"""

import requests
from docopt import docopt

base_url = 'http://127.0.0.1:3000/tickets'


def show(args):
    global res
    if args['--page']:
        print('Showing page # {0}'.format(args['--page']))
        param = {'page': '{0}'.format(args['--page'])}
        res = requests.get(base_url, param)

    elif args['<ticket>']:
        print('Showing ticket # {0}:'.format(args['<ticket>']))
        res = requests.get('http://127.0.0.1:3000/tickets/{0}'.format(args['<ticket>']))
    else:
        print('Showing page # 1')
        res = requests.get(base_url)
    print_result()


def print_result():
    if res.status_code == 200:
        print(res.json())
    else:
        print(res)


# def auth():
#         dmn = raw_input("domain:")
#         usr = raw_input("username(email):")
#         pswd = getpass.getpass('password:')
#         return dmn, usr, pswd


if __name__ == '__main__':
    args = docopt(__doc__)


if args['show']:
    show(args)
