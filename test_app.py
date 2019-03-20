"""Tests for Parser"""

import os
from unittest import TestCase
from app import read_formats
from sample_data import test_case_data

VALID_FILE = 'test_formats_valid.csv'
INVALID_FILE = 'test_formats_INvalid.csv'

class AppTestCase(TestCase):
    """Test read file function"""

    def setUp(self):
        # create valid format csv file
        with open(VALID_FILE, 'w+') as f:
            for i, _format in enumerate(test_case_data['valid_formats']):
                f.write(_format)
                if i < len(test_case_data['valid_formats'])-1:
                    f.write('\n')
        
        # create valid format csv file
        with open(INVALID_FILE, 'w+') as f:
            for i, _format in enumerate(test_case_data['invalid_formats']):
                f.write(_format)
                if i < len(test_case_data['invalid_formats'])-1:
                    f.write('\n')

    def test_read_formats(self):
        """Can read valid formats?"""

        valid_formats = read_formats(VALID_FILE)
        self.assertTrue(isinstance(valid_formats, list))
        
    def test_read_formats_errors(self):
        """Throws error with invalid formats?"""
        with self.assertRaises(KeyError):
            read_formats(INVALID_FILE)
        
    def tearDown(self):
        try:
            os.remove(VALID_FILE)
            os.remove(INVALID_FILE)
        except FileNotFoundError:
            pass
        return super().tearDown()