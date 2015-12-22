import os
import unittest
import tempfile

import gief


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = gief.app.test_client()

    def test_get(self):
        rv = self.app.get('/')
        assert b'Upload' in rv.data

    def test_post_without_file(self):
        rv = self.app.post('/')
        assert rv.status_code == 400


if __name__ == '__main__':
    unittest.main()
