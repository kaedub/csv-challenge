import re
from config import ZIP_LENGTH, PHONE_LENGTH

def is_name(name):
    return ''.join(name.split(' ')).isalpha()

def is_zip(zip):
    """Returns true if 'zip' is a valid zip code"""
    return zip.isdigit() and len(zip) == 5

def is_phone_hyphenated(phone):
    """Returns true if 'phone' is a valid phone number with parentheses and hyphens"""
    phone_regex = r'[\(]{1}[0-9]{3}[\)]{1}[\-]{1}[0-9]{3}[\-]{1}[0-9]{4}'
    match = re.match(phone_regex, phone)
    if not match:
        return False
    return match.span() == (0,len(phone))

def is_phone_spaced(phone):
    """Returns true if 'phone' is a valid phone number with spaces instead of dashes and parentheses"""
    phone_regex = r'[0-9]{3}[ ]{1}[0-9]{3}[ ]{1}[0-9]{4}'
    match = re.match(phone_regex, phone)
    if not match:
        return False
    return match.span() == (0,len(phone))

field_validators = {
    "lastname": is_name,
    "firstname": is_name,
    "fullname": is_name,
    "color": is_name,
    "phone_hyphenated":  is_phone_hyphenated,
    "phone_spaced": is_phone_spaced,
    "zip": is_zip
}

def validate_line(line, formats):
    """Return True if 'line' matches any format in 'formats'"""
    for _format in formats:
        if is_line_formatted(line, _format):
            return True
    return False
    
def is_line_formatted(line, _format):
    """Return True if 'line' matches '_format'"""
    if len(line) != len(_format):
        return False
    else:
        for i in range(len(line)):
            print("i", i)
            print(line[i], _format[i])
            valid_field = field_validators[_format[i]](line[i])
            print('valid', valid_field)
            if not valid_field:
                return False
    return True



