import sys
from config import DATA_FILENAME, FORMATS_FILENAME, OUTPUT_FILENAME
from validation import field_validators
from parser import Parser

def read_formats(filename):
    """Reads formats from a csv file"""
    formats = []
    with open(filename, encoding="utf8") as f:
        for line in f.read().split('\n'):
            format_fields = line.strip().split(',')
            # a first and last name or full name are required
            if not set(["lastname", "firstname"]).issubset(format_fields) and "fullname" not in format_fields:
                raise KeyError('All formats must contain "firstname" and "lastname" fields or "fullname" field.')
            for field_name in format_fields:
                if field_name not in field_validators.keys():
                    raise KeyError(f'Validator function for "{field_name}" not found. Did you add it to validators?')
            formats.append(format_fields)
    return formats

def create_parser():
    """Factory function that builds and returns a PersonalInfoParser instance"""
    
    formats = read_formats(FORMATS_FILENAME)
    parser = Parser(DATA_FILENAME, field_validators, formats)

    return parser

if __name__ == "__main__":
    parser = create_parser()
    parser.parse()
    parser.json_to_file()

