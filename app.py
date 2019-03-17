from csv import DictReader, DictWriter
import sys

# formats:
# A - lastname, firstname, phone-closed, color, zip
# B - fullname, color, zip, phone-open
# C - firstname, lastname, zip, phone-open, color

class LineValidator():
    def __init__(self, formats=""):
        self.formats = formats

    def is_color(self, s):
        """Returns true if 's' is a valid color"""
        pass

    def _is_closed_phone_number(self, phone):
        """Returns true if 'phone' is a valid phone number with parentheses and dashes"""
        pass

    def _is_open_phone_number(self, phone):
        """Returns true if 'phone' is a valid phone number without parenthesis or dashes"""
        pass

    def is_phone_number(self, phone):
        """Returns true if 'phone' is a valid phone number"""
        return self._is_closed_phone_number or self._is_open_phone_number
    
    def is_zip(self, zip):
        """Returns true if 'zip' is a valid zip code"""
        return zip.isdigit() and len(zip) == 5

class FileReader():
    def __init__(self, filename):
        self.filename = filename

    def read_file(filename):
        """Returns the master inventory as a dictionary."""
        cache = {}
        validator = LineValidator()
        with open(filename, encoding="utf8") as f:
            line = f.readline()
            while line != '':
                print(line)
                line = f.readline()
        return cache