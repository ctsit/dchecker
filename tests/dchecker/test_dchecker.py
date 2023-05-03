import unittest

from dchecker import is_safe_request


class TestCredentials(unittest.TestCase):
    def test_is_safe_request(self):
        # https
        self.assertTrue(is_safe_request("https://example.com", "email@example.com", "password"))
        self.assertTrue(is_safe_request("https://example.com", "email@example.com", ""))
        self.assertTrue(is_safe_request("https://example.com", "", "password"))
        self.assertTrue(is_safe_request("https://example.com", "", ""))
        # http
        self.assertTrue(is_safe_request("http://example.com", "", ""))
        self.assertFalse(is_safe_request("http://example.com", "email@example.com", "password"))
        self.assertFalse(is_safe_request("http://example.com", "", "password"))
        self.assertFalse(is_safe_request("http://example.com", "email@example.com", ""))


if __name__ == '__main__':
    unittest.main()
