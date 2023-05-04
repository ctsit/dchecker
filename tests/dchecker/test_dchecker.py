import unittest

from dchecker import is_safe_request


class TestCredentials(unittest.TestCase):
    def test_is_safe_request(self):
        # https
        self.assertTrue(is_safe_request("https://example.com", "email@example.com", "password"))
        self.assertTrue(is_safe_request("https://example.com", "email@example.com", ""))
        self.assertTrue(is_safe_request("https://example.com", "email@example.com", None))
        self.assertTrue(is_safe_request("https://example.com", "", "password"))
        self.assertTrue(is_safe_request("https://example.com", None, "password"))
        self.assertTrue(is_safe_request("https://example.com", "", ""))
        self.assertTrue(is_safe_request("https://example.com", None, None))

        # localhost
        self.assertTrue(is_safe_request("http://localhost", "email@example.com", "password"))
        self.assertTrue(is_safe_request("http://localhost", "email@example.com", ""))
        self.assertTrue(is_safe_request("http://localhost", "email@example.com", None))
        self.assertTrue(is_safe_request("http://localhost", "", "password"))
        self.assertTrue(is_safe_request("http://localhost", None, "password"))
        self.assertTrue(is_safe_request("http://localhost", "", ""))
        self.assertTrue(is_safe_request("http://localhost", None, None))

        # http
        self.assertTrue(is_safe_request("http://example.com", "", ""))
        self.assertTrue(is_safe_request("http://example.com", None, None))
        self.assertFalse(is_safe_request("http://example.com", "email@example.com", "password"))
        self.assertFalse(is_safe_request("http://example.com", "", "password"))
        self.assertFalse(is_safe_request("http://example.com", None, "password"))
        self.assertFalse(is_safe_request("http://example.com", "email@example.com", ""))
        self.assertFalse(is_safe_request("http://example.com", "email@example.com", None))


if __name__ == '__main__':
    unittest.main()
