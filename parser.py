from validation import field_validators

class PersonalInfoParser():
    def __init__(self, filename):
        """Create an instance that will parse the filename passed to the constructor"""

        self.data_file = filename
        self.formats = []
        self.entries = []
        self.errors = []

    def _is_line_formatted(self, line, _format):
        """Return True if 'line' matches '_format'"""

        if len(line) != len(_format):
            return False
        else:
            # if any field is invalid, fail
            for i in range(len(line)):
                field_value = line[i].strip()
                field_name = _format[i]
                try:
                    validate = field_validators[field_name]
                except KeyError as e:
                    raise KeyError(f'Validator function for "{field_name}" not found. Did you add it to the field_validators dictionary?')
                if not validate(field_value):
                    return False
        return True

    def _parse_field(self, name, value):
        """Return a parsed field as a dictionary with appropriate keys"""

        # this is a slightly hardcoded solution to handle complex fields
        # an extensible solution should handle field names dynamically
        if name == "fullname":
            firstname = " ".join(value.split(' ')[:-1])
            lastname = value.split(' ')[-1]
            field = { "firstname": firstname, "lastname": lastname}
        elif name == "phone_hyphenated":
            phone = value[1:4] + value[5:]
            field = { "phonenumber": phone}
        elif name == "phone_spaced":
            phone = '-'.join(value.split(' '))
            field = { "phonenumber": phone}
        else:
            field = {name: value}
        return field

    def _match_line_to_format(self, line):
        """
        Matches a line with a format and returns a dictionary.
        
        Returns False if 'line' does not match any format in 'formats'
        """

        for fields in self.formats:
            if self._is_line_formatted(line, fields):
                row = {}
                for i, key in enumerate(fields):
                    value = line[i]
                    field_dict = self._parse_field(key, value)
                    row = {**row, **field_dict}
                return row
        return False
    
    def load_formats(self, filename):
        """Load formats from csv file"""

        with open(filename, encoding="utf8") as f:
            self.formats = [line.split(',') for line in f.read().split('\n')]
        return self.formats

    def parse(self):
        """Returns the master inventory as a dictionary"""

        with open(self.data_file, encoding="utf8") as f:
            line = f.readline()
            line_num = 0
            while line != '':
                line = [field.strip() for field in line.split(',')]

                # map line to field names
                line = self._match_line_to_format(line)
                if line:
                    self.entries.append(line)
                else:
                    self.errors.append(line_num)
                line = f.readline()
                line_num += 1

        return { "entries": self.entries, "errors": self.errors }

    def to_json(self):
        """Return a json string that is sorted and indented two spaces"""

        json_string = '{\n'
        json_string += '  "entries": [\n'
        field_names = list(self.entries[0].keys())
        field_names.sort()

        sorted_entres = sorted(self.entries, key = lambda e: (e['lastname'], e['firstname']))

        for i, entry in enumerate(sorted_entres):
            json_string += '    {\n'
            for j, name in enumerate(field_names):
                json_string += f'      "{name}": "{entry[name]}"'
                json_string += ',\n' if j < len(field_names)-1 else '\n'
            json_string += '    '
            json_string += '},\n' if i < len(self.entries)-1 else '}\n'

        json_string += '  ],\n'

        json_string += '  "errors": [\n'
        for i, error in enumerate(self.errors):
            json_string += f'    {error}'
            json_string += ',\n' if i < len(self.errors)-1 else '\n'
            pass
        json_string += '  ]\n'
        json_string += '}\n'
        return json_string
    
    def json_to_file(self, filename):
        """Write json to file"""

        with open(filename, 'w+') as f:
            f.write(self.to_json())
    
    def __repr__(self):
        return f'<FileReader data_file: {self.data_file} entries: {len(self.entries)} errors: {len(self.errors)} formats: {len(self.formats)}>'

