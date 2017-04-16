import unittest

from url import get_url


class UrlCreationTestCase(unittest.TestCase):
    def test_get_url_no_param(self):
        arguments = {'--help': False, '--page': None, '<ticket>': None, 'show': True}
        self.assertEqual(get_url(arguments), 'http://127.0.0.1:3000/tickets')

    def test_get_url_ticket(self):
        arguments = {'--help': False, '--page': None, '<ticket>': '0', 'show': True}
        self.assertEqual(get_url(arguments), "http://127.0.0.1:3000/tickets/0")

    def test_get_url_page(self):
        arguments = {'--help': False, '--page': 1, '<ticket>': None, 'show': True}
        self.assertEqual(get_url(arguments), ("http://127.0.0.1:3000/tickets", {'page': '1'}))
