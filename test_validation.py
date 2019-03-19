"""Tests for validation"""

import os
from unittest import TestCase

from validation import is_phone_spaced, is_phone_hyphenated, is_name, is_zip
from sample_data import test_case_data

class ValidationTestCase(TestCase):
    """Test read file function"""
    def setUp(self):
        pass

    def test_is_phone_spaced(self):
        """Can validate a phone number with spaced format?"""
        
        # do valid spaced format phone numbers work?
        for phone in test_case_data.get('valid_phones_spaced'):
            self.assertTrue(
                is_phone_spaced(phone),
                f'"{phone}" is not a valid phone number')
        
        # do invalid phone numbers fail?
        for phone in test_case_data.get('invalid_phones'):
            self.assertFalse(
                is_phone_spaced(phone), 
                f'"{phone}" is not a invalid phone number')
        
        # do phone numbers for other valid formats fail?
        for phone in test_case_data.get('valid_phones_hyphenated'):
            self.assertFalse(
                is_phone_spaced(phone), 
                f'"{phone}" is not a invalid phone number')
    
    def test_is_phone_hyphenated(self):
        """Can validate a phone number with hyphenated format?"""
        
        # do valid hyphenated format phone numbers work?
        for phone in test_case_data.get('valid_phones_hyphenated'):
            self.assertTrue(
                is_phone_hyphenated(phone),
                f'"{phone}" is not a valid phone number')
        
        # do invalid phone numbers fail?
        for phone in test_case_data.get('invalid_phones'):
            self.assertFalse(
                is_phone_hyphenated(phone), 
                f'"{phone}" is not an invalid phone number')
        
        # do phone numbers for other valid formats fail?
        for phone in test_case_data.get('valid_phones_spaced'):
            self.assertFalse(
                is_phone_hyphenated(phone), 
                f'"{phone}" is not an invalid phone number')

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
    
    # def test_is_row_formatted(self):
    #     """Can validate a entry with a format?"""

    #     entry = [field.strip() for field in test_case_data.get('valid_entries')[0].split(',')]
    #     _format = test_case_data.get('valid_formats')[0].split(',')
    #     valid = is_row_formatted(entry, _format)
    #     self.assertTrue(valid, f'{entry} is not of a valid format')

    # def test_validate_row(self):
    #     """Can validate a entry with a list of formats?"""

    #     entry = test_case_data.get('valid_entries')[0].split(',')
    #     formats = [_format.split(',') for _format in test_case_data.get('valid_formats')]
    #     valid = validate_row(entry, formats)
    #     self.assertTrue(valid, f'{entry} is not of a valid format')
