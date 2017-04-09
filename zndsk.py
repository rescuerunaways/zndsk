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

from docopt import docopt
import requests

def show(args):
    global res
    if(args['--page']):
        print('Showing page # {0}'.format(args['--page']))
        param = {'page': '{0}'.format(args['--page'])}
        res = requests.get('http://127.0.0.1:3000/tickets', param)

    elif(args['<ticket>']):
        print('Showing ticket # {0}:'.format(args['<ticket>']))
        res = requests.get('http://127.0.0.1:3000/ticket/{0}'.format(args['<ticket>']))
    else:
        print('Showing page # 1')
        res = requests.get('http://127.0.0.1:3000/tickets')
    printResult()

def printResult ():
    if (res.status_code == 200):print(res.json())
    else: print(res)


# def auth():
#         dmn = raw_input("domain:")
#         usr = raw_input("username(email):")
#         pswd = getpass.getpass('password:')
#         return dmn, usr, pswd


if __name__ == '__main__':
    args = docopt(__doc__)


if args['show']:
    show(args)
