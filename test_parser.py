"""Tests for PersonalInfoParser"""

import os
from unittest import TestCase
from parser import PersonalInfoParser

FILENAME = 'data.csv'

class PersonalInfoParserTestCase(TestCase):
    """Test read file function"""

    def setUp(self):
        self.parser = PersonalInfoParser()

    def test_is_line_formatted(self):
        """Can check if a line is of a valid format?"""

        pass

    def test_parse_field(self):
        """Can parse a single field into a dictionary?"""
        pass

    def test_map_line_to_format(self):
        """
        pass

    def test_load_formats(self):
        pass

    def test_parse(self):
        pass

    def test_to_json(self):
        pass

    def test_json_to_file(self):
        pass

