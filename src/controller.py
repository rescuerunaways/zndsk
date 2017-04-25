from json import dumps

import requests

from src.url import get_url


def get(args):
    res = requests.get(*get_url(args))
    if not res.ok:
        return dumps("Server error:{0}".format(Exception(res.reason, res.status_code)))
    return res
