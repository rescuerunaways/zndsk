import unittest

from controller import get


class UrlCreationTestCase(unittest.TestCase):
    def test_no_param(self):
        args = {'--page': None, '<ticket>': None, 'show': True}
        res = get(args)
        self.assertFalse("Server error" in res.json())

    def test_get_ticket(self):
        args = {'--page': None, '<ticket>': '1', 'show': True}
        res = get(args)
        self.assertEqual(res.json()[0]['id'], 1)

    def test_page(self):
        args = {'--page': '1', '<ticket>': None, 'show': True}
        res = get(args)
        self.assertFalse("Server error" in res.json())

    def test_non_present_ticket(self):
        args = {'--page': None, '<ticket>': '999999999999', 'show': True}
        res = get(args)
        self.assertTrue("Server error", "404" in res.json())

    def test_non_present_page(self):
        args = {'--page': '999999999999', '<ticket>': None, 'show': True}
        res = get(args)
        self.assertFalse(res.json())
