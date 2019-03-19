import re
from config import ZIP_LENGTH, PHONE_LENGTH

def is_name(string):
    """Returns True if 'string' is a valid name (contains only letters and whitespace)"""
    
    # convert hyphenate names
    string = re.sub('-', ' ', string)
    return ''.join(string.split(' ')).isalpha()

def is_zip(zip):
    """Returns true if 'zip' is a valid zip code"""

    return zip.isdigit() and len(zip) == 5

def is_phone_hyphenated(phone):
    """Returns true if 'phone' is a valid phone number with parentheses and hyphens"""

    phone_regex = r'[\(][\d]{3}[\)][\-][\d]{3}[\-][\d]{4}'
    match = re.match(phone_regex, phone)
    if not match:
        return False
    return match.span() == (0,len(phone))

def is_phone_spaced(phone):
    """Returns true if 'phone' is a valid phone number with spaces instead of dashes and parentheses"""
    
    phone_regex = r'[\d]{3}[ ][\d]{3}[ ][\d]{4}'
    match = re.match(phone_regex, phone)
    if not match:
        return False
    return match.span() == (0,len(phone))

# map field types to a validator function
field_validators = {
    "lastname": is_name,
    "firstname": is_name,
    "fullname": is_name,
    "color": is_name,
    "phone_hyphenated":  is_phone_hyphenated,
    "phone_spaced": is_phone_spaced,
    "zipcode": is_zip
}




