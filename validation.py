import re

def is_name(name):
    """Returns True if a is a valid name (contains only letters, hyphens, periods, and whitespace)"""

    # valid names can have hyphens, whitespace, and periods
    name = re.sub(r'[-. ]', '', name)
    return name.isalpha()

def is_zip(zip):
    """Returns true if a string is a valid 5 digit integer zip code"""

    return zip.isdigit() and len(zip) == 5

def is_phone_hyphenated(phone):
    """Returns true if a string is a valid 10 digit phone number with parentheses and hyphens"""

    phone_regex = r'[\(][\d]{3}[\)][\-][\d]{3}[\-][\d]{4}'
    match = re.match(phone_regex, phone)
    if not match:
        return False
    return match.span() == (0,len(phone))

def is_phone_spaced(phone):
    """Returns true if a string is a valid 10 digit phone number with spaces instead of dashes and parentheses"""
    
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
