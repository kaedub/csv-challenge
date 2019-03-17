"""Tests for validation"""

import os
from unittest import TestCase

from validation import is_phone, is_name, is_zip
from sample_data import test_case_data


# NOTES:
# Is '7037420996' to be considerd an invalid phone number?

class ValidationTestCase(TestCase):
    """Test read file function"""
    def setUp(self):
        pass

    def test_validate_phone(self):
        """Can validate a phone number?"""
        
        for phone in test_case_data.get('valid_phones'):
            self.assertTrue(
                is_phone(phone),
                f'{phone} is not a valid phone number')
        
        for invalid_phone in test_case_data.get('invalid_phones'):
            self.assertFalse(
                is_phone(invalid_phone), 
                f'{invalid_phone} is not a valid phone number')

    # def test_validate_zip(self):
    #     """Can validate a zip code?"""
        
    #     for zip in test_case_data.get('valid_zips'):
    #         self.assertTrue(is_zip(zip))
    #     for zip in test_case_data.get('invalid_zips'):
    #         self.assertFalse(is_zip(zip))

    # def test_validate_name(self):
    #     """Can validate a name?"""
        
    #     for name in test_case_data.get('valid_names'):
    #         self.assertTrue(is_name(name))
    #     for name in test_case_data.get('invalid_names'):
    #         self.assertFalse(is_name(name))
