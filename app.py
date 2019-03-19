import sys
from config import DATA_FILENAME, FORMATS_FILENAME
from validation import validate_line

# formats:
# A - lastname, firstname, phone-closed, color, zip
# B - fullname, color, zip, phone-open
# C - firstname, lastname, zip, phone-open, color

class PersonalInfoParser():
    def __init__(self, filename):
        """Create an instance that will parse the filename passed to the constructor"""
        self.data_filename = filename
        self.formats = []
        self.lines = []
        self.errors = []
    
    def load_formats(self, filename):
        """Load formats from file"""
        with open(filename, encoding="utf8") as f:
            self.formats = [line.split(',')[:-1] for line in f.read().split('\n')]
        return self.formats


    def read(self):
        """Returns the master inventory as a dictionary."""
        with open(self.filename, encoding="utf8") as f:
            line = f.readline()
            line_num = 0
            while line != '':
                if validate_line(line):
                    self.lines.append(line)
                else:
                    self.errors.append(line_num)
                line = f.readline()
                line_num += 1
        return self.lines
    
    def __repr__(self):
        return f'<FileReader filename: {self.filename} lines: {len(self.lines)}>'

def create_parser():
    """Factory function that builds and returns a PersonalInfoParser instance"""
    parser = PersonalInfoParser(DATA_FILENAME)
    parser.load_formats(FORMATS_FILENAME)

    return parser

if __name__ == "__main__":
    parser = create_parser()
    pi_data = parser.read()
    print(pi_data)
    # [print(line) for line in reader.lines]