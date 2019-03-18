"""Tests for validation"""

import os
from unittest import TestCase

from validation import is_phone_spaced, is_phone_hyphenated, is_name, is_zip, is_line_formatted, validate_line
from sample_data import test_case_data


# NOTES:
# Is '7037420996' to be considerd an invalid phone number?

class ValidationTestCase(TestCase):
    """Test read file function"""
    def setUp(self):
        pass

    def test_is_phone_spaced(self):
        """Can validate a phone number with spaced format?"""
        
        for phone in test_case_data.get('valid_phones_spaced'):
            self.assertTrue(
                is_phone_spaced(phone),
                f'"{phone}" is not a valid phone number')
        
        # test that invalid phone numbers fail
        for phone in test_case_data.get('invalid_phones'):
            self.assertFalse(
                is_phone_spaced(phone), 
                f'"{phone}" is not a valid phone number')
        
        # test that hyphenated phone numbers fail
        for phone in test_case_data.get('valid_phones_hyphenated'):
            self.assertFalse(
                is_phone_spaced(phone), 
                f'"{phone}" is not a valid phone number')
    
    def test_is_phone_hyphenated(self):
        """Can validate a phone number with hyphenated format?"""
        
        for phone in test_case_data.get('valid_phones_hyphenated'):
            self.assertTrue(
                is_phone_hyphenated(phone),
                f'"{phone}" is not a valid phone number')
        
        for phone in test_case_data.get('invalid_phones'):
            self.assertFalse(
                is_phone_hyphenated(phone), 
                f'"{phone}" is not a valid phone number')
        
        for phone in test_case_data.get('valid_phones_spaced'):
            self.assertFalse(
                is_phone_hyphenated(phone), 
                f'"{phone}" is not a valid phone number')

    def test_is_zip(self):
        """Can validate a zip code?"""
        
        for zip in test_case_data.get('valid_zips'):
            self.assertTrue(is_zip(zip), f'"{zip}" is not a valid zip code')
        for zip in test_case_data.get('invalid_zips'):
            self.assertFalse(is_zip(zip), f'"{zip}" is not a valid zip code')

    def test_is_name(self):
        """Can validate a name?"""
        
        for name in test_case_data.get('valid_names'):
            self.assertTrue(is_name(name), f'"{name}" is not a valid name')
        for name in test_case_data.get('invalid_names'):
            self.assertFalse(is_name(name), f'"{name}" is not a valid name')
    
    # def test_is_line_formatted(self):
    #     """Can validate a line with a format?"""

    #     line = test_case_data.get('valid_lines')[0].split(',')
    #     _format = test_case_data.get('valid_formats')[0].split(',')
    #     print("Test input", line, _format)
    #     valid = is_line_formatted(line, _format)
    #     self.assertTrue(valid, f'{line} is not a valid format')

    # def test_validate_line(self):
    #     """Can validate a line with a list of formats?"""

    #     line = test_case_data.get('valid_lines')[0].split(',')
    #     formats = test_case_data.get('valid_formats')
    #     valid = validate_line(line, formats)
    #     self.assertTrue(valid, f'{line} is not a valid format')
