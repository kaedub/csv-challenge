import sys
from config import DATA_FILENAME, FORMATS_FILENAME

# formats:
# A - lastname, firstname, phone-closed, color, zip
# B - fullname, color, zip, phone-open
# C - firstname, lastname, zip, phone-open, color

def parse_formats(filename):
    formats = []
    with open(filename) as f:
        pass

# Normalize
#   FileReader
#   LineParser and Validation
#   Sorter
#   JSONWriter

class FileReader():
    def __init__(self, filename):
        self.filename = filename
        self.lines = []
        self.errors = []

    def read(self):
        """Returns the master inventory as a dictionary."""

        with open(self.filename, encoding="utf8") as f:
            
            line = f.readline()

            while line != '':
                # read each line
                self.lines.append(line)

                # remove invalid lines

                line = f.readline()
        return self.lines
    
    def __repr__(self):
        return f'<FileReader filename: {self.filename} lines: {len(self.lines)}>'

if __name__ == "__main__":
    reader = FileReader(DATA_FILENAME)
    reader.read()
    print(reader)
    [print(line) for line in reader.lines]