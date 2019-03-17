from config import ZIP_LENGTH, PHONE_LENGTH

def is_name(name):
    return ''.join(name.split(' ')).isalpha()

def is_phone(phone):
    """Returns true if 'phone' is a valid phone number"""
    return _is_phone_spaced(phone) or _is_phone_hyphenated(phone)

def is_zip(zip):
    """Returns true if 'zip' is a valid zip code"""
    return zip.isdigit() and len(zip) == 5

def _is_phone_hyphenated(phone):
    """Returns true if 'phone' is a valid phone number with parentheses and hyphens"""
    stripped = ''.join(phone.split('-'))
    if len(stripped) < PHONE_LENGTH+2:
        return False
    elif stripped[0] != '(' and stripped[4] != ')':
        return False
    raw_phone = stripped[1:4] + stripped[5:]
    return raw_phone.isdigit() and len(raw_phone) == PHONE_LENGTH

def _is_phone_spaced(phone):
    """Returns true if 'phone' is a valid phone number with spaces instead of dashes and parentheses"""
    raw_phone = ''.join(phone.split(' '))
    return len(raw_phone) == 10 and raw_phone.isdigit()
