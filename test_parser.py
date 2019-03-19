"""Reader tests."""

import os
from unittest import TestCase

from app import read_file

FILENAME = 'data.csv'

class ReadFileTestCase(TestCase):
    """Test read file function"""

    def setUp(self):
        pass


    def test_add_message(self):
        """Can read a csv file?"""

        out = read_file(FILENAME)

        self.assertEqual(out, {})
