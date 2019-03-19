import sys
from config import DATA_FILENAME, FORMATS_FILENAME, OUTPUT_FILENAME
from parser import PersonalInfoParser

def create_parser():
    """Factory function that builds and returns a PersonalInfoParser instance"""
    parser = PersonalInfoParser(DATA_FILENAME)
    parser.load_formats(FORMATS_FILENAME)
    return parser

if __name__ == "__main__":
    parser = create_parser()
    parser.parse()
    parser.json_to_file(OUTPUT_FILENAME)

