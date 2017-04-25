import unittest

from src.const import *
from src.url import get_url


class UrlCreationTestCase(unittest.TestCase):
    # @data_provider(itemIds)
    def test_get_url_no_param(self):
        arguments = {'--help': False, '--page': None, '<ticket>': None, 'show': True}
        self.assertEqual(get_url(arguments), (TICKETS_ULR,))

    def test_get_url_ticket(self):
        arguments = {'--help': False, '--page': None, '<ticket>': '1', 'show': True}
        self.assertEqual(get_url(arguments), (TICKETS_ULR + "/1",))

    def test_get_url_page(self):
        arguments = {'--help': False, '--page': 1, '<ticket>': None, 'show': True}
        self.assertEqual(get_url(arguments), (TICKETS_ULR, {'page': '1'}))
