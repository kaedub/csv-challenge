"""Integration tests for Parser"""

import os
from unittest import TestCase
from parser import Parser
from sample_data import test_case_data
from validation import field_validators

DATA_FILE = 'test.csv'
JSON_FILE = 'test.json'

class ParserTestCase(TestCase):
    """Test read file function"""

    def setUp(self):
        # create a test.csv file with valid and invalid entries
        with open(DATA_FILE, 'w+') as f:
            [f.write(_format+'\n') for _format in test_case_data['valid_entries']]
            [f.write(_format+'\n') for _format in test_case_data['invalid_entries']]
        
        # create a list of valid formats
        formats = [f.split(',') for f in test_case_data['valid_formats']]
        self.parser = Parser(DATA_FILE, field_validators, formats)

    def test_is_entry_formatted(self):
        """Can check if a entry is of a valid format?"""

        valid_formats = test_case_data.get('valid_formats')
        for i, valid_entry in enumerate(test_case_data.get('valid_entries')):
            entry = [value.strip() for value in valid_entry.split(',')]
            format_fields = valid_formats[i].split(',')
            valid = self.parser._is_entry_formatted(entry, format_fields)
            self.assertTrue(valid, f'{entry} is not of a valid format')

        # fails with invalid entries
        for invalid_entry in test_case_data.get('invalid_entries'):
            entry = [value.strip() for value in invalid_entry.split(',')]
            for f in valid_formats:
                format_fields = f.split(',')
                entry_dict = self.parser._is_entry_formatted(entry, format_fields)
                self.assertFalse(entry_dict, f'{entry} is not of a valid format')


    def test_match_entry_to_format(self):
        """Can match an entry to a format?"""

        # matches valid entries with valid formats
        for valid_entry in test_case_data.get('valid_entries'):
            entry = [e.strip() for e in valid_entry.split(',')]
            entry_dict = self.parser._match_entry_to_format(entry)

            self.assertTrue(entry_dict, f'{entry} is not of a valid format')

        # fails with invalid entries
        for invalid_entry in test_case_data.get('invalid_entries'):
            entry = [e.strip() for e in invalid_entry.split(',')]
            entry_dict = self.parser._match_entry_to_format(entry)

            self.assertFalse(entry_dict, f'{entry} is not of a valid format')



    def test_parse_field(self):
        """Can parse a single field into a dictionary?"""
        
        # parses valid fields
        field = self.parser._parse_field('fullname', 'John Doe')
        self.assertEqual(field, {'firstname': 'John', 'lastname': 'Doe'})

        field = self.parser._parse_field('phone_hyphenated', '(703)-742-0996')
        self.assertEqual(field, {'phonenumber': '703-742-0996'})

        field = self.parser._parse_field('phone_spaced', '703 742 0996')
        self.assertEqual(field, {'phonenumber': '703-742-0996'})

        field = self.parser._parse_field('firstname', 'Billy Bob')
        self.assertEqual(field, {'firstname': 'Billy Bob'})

        # returns empty dict for invalid fields
        field = self.parser._parse_field('age', 44)
        self.assertEqual(field, {})

        field = self.parser._parse_field('nickname', 'hackerman')
        self.assertEqual(field, {})

    def test_parse(self):
        """Can parse a csv file with valid and invalid rows?"""     

        results = self.parser.parse()
        self.assertEqual(results, test_case_data['parse_output'])

    def test_to_json(self):
        """Can output a valid JSON string that is sorted and indented two spaces"""

        self.parser.parse()
        json_string = self.parser.to_json()
        
        self.assertTrue(isinstance(json_string, str))

    def test_json_to_file(self):
        """Can write valid JSON to a file that is sorted and indented two spaces"""

        self.parser.parse()
        self.parser.json_to_file(JSON_FILE)
        json_string = self.parser.to_json()

        with open(JSON_FILE) as f:
            json_file_string = f.read()
        
        self.assertEqual(json_string, json_file_string)

    def tearDown(self):
        try:
            os.remove(DATA_FILE)
            os.remove(JSON_FILE)
        except FileNotFoundError:
            pass
        return super().tearDown()