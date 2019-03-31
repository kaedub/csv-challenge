"""Personal Information Parser"""

class Parser():
    def __init__(self, data_file, validators, formats=[]):
        """Create an instance that will parse a data file using an list of formats.
        
        @param data_file: filename for csv data file
        @param formats: list of formats
        
        All formats must have a fullname field, or firstname and lastname fields.

        All format fields must be exist in field_validators with a validation function.
        
        example formats list:
        [
            ['lastname', 'firstname', 'phone_hyphenated', 'color', 'zipcode'], 
            ['fullname', 'color', 'zipcode', 'phone_spaced'], 
            ['firstname', 'lastname', 'zipcode', 'phone_spaced', 'color']
        ]
        """

        self.data_file = data_file
        self.formats = formats
        self.validators = validators
        self.entries = []
        self.errors = []

    def _parse_field(self, name, value):
        """Returns a dictionary containing the names and values of a field and handles
        compound fields and special fields - fullname, phone_spaced, and phone_hyphenated
        
        @param name: string for field name
        @param value: string for field value
        """

        # this is a slightly hardcoded solution to handle complex fields
        # an extensible solution should handle field names dynamically
        field = {}
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
        elif name in self.validators.keys():
            field = {name: value}
            
        return field

    def _is_entry_formatted(self, line, format_fields):
        """Return True if line matches format_fields
        
        @param line: list of field values
        @param format_fields: list of field names

        """

        if len(line) != len(format_fields):
            return False
        else:
            # validate that each field in the line matches the format fields
            for i in range(len(line)):
                field_value = line[i].strip()
                field_name = format_fields[i]
                try:
                    validate = self.validators[field_name] # get validator function for field
                except KeyError:
                    raise KeyError(
                        f'Validator function for "{field_name}" not found. Did you add it to validators?'
                    )
                if not validate(field_value):
                    return False
        return True

    def _match_entry_to_format(self, entry):
        """Matches a entry with a format and returns a dictionary.
        
        Returns empty dict if entry does not match any format in self.formats.

        @param entry: list of field values
        """

        for fields in self.formats:
            if self._is_entry_formatted(entry, fields):
                row = {}
                for i, key in enumerate(fields):
                    value = entry[i]
                    field_dict = self._parse_field(key, value)
                    row = {**row, **field_dict}
                return row
        return {}

    def parse(self):
        """Returns a dictionary of entries and errors parsed from the data file"""

        with open(self.data_file, encoding="utf8") as f:
            line = f.readline()
            line_num = 0
            while line != '':
                line = [field.strip() for field in line.split(',')]

                # map line to field names
                line = self._match_entry_to_format(line)

                if line:
                    self.entries.append(line)
                else:
                    self.errors.append(line_num)
                line = f.readline()
                line_num += 1
        return { "entries": self.entries, "errors": self.errors }

    def to_json(self):
        """Return a json string that is sorted by lastname,firstname and indented two spaces"""

        json_string = '{\n'
        json_string += '  "entries": [\n'

        # sort entries
        sorted_entries = sorted(self.entries, key = lambda e: (e['lastname'], e['firstname']))

        for i, entry in enumerate(sorted_entries):
            # sort keys in entry
            field_names = list(entry.keys())
            field_names.sort()
            
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
    
    def json_to_file(self, filename='result.json'):
        """Write json to file
        
        @param filename: string for filename of result json file
        """

        with open(filename, 'w+') as f:
            f.write(self.to_json())
    
    def __repr__(self):
        return f'<FileReader data_file: {self.data_file} json_file: {self.json_file} entries: {len(self.entries)} errors: {len(self.errors)} formats: {len(self.formats)}>'

