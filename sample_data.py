test_case_data = {
    "valid_entries": [
        "Smith, John, (623)-668-9293, yellow, 87360",
        "James Murphy, yellow, 83880, 018 154 6474",
        "Booker T., Washington, 87360, 373 781 7380, yellow",
    ],
    "invalid_entries": [
        "Smith, John, (623) 668-9293, yellow, 87360",
        "James Murphy, 83880, yellow, 018 154 6474",
        "Booker T., Washington, 87360, 3737817380",
        "98sd982jsf",
        "1,2,3,4,5",
    ],
    "valid_formats": [
        "lastname,firstname,phone_hyphenated,color,zipcode",
        "fullname,color,zipcode,phone_spaced",
        "firstname,lastname,zipcode,phone_spaced,color"
    ],
    "invalid_formats": [
        "address,phone,zip",
        "color,zipcode,phone_spaced",
        "firstname,lastname",
        "lastname,zipcode,phone_spaced,color"
    ],
    "valid_phones_hyphenated": [
        '(703)-742-0996',
        '(646)-111-0101',
        '(703)-955-0373',
    ],
    "valid_phones_spaced": [
        '703 742 0996',
        '646 111 0101',
        '703 955 0373',
    ],
    "invalid_phones": [
        '(703) 742 0996',
        '646-111-0101',
        '955 0373',
        # '7037420996',
        'adoijfw',
        '(703) 742 099'
    ],
    "valid_zips": [
        '10013',
        '95223',
        '94122'
    ],
    "invalid_zips": [
        '100134',
        'a5223',
        '904a3',
        'hello',
        '1001',
        '1001347465365',
    ],
    "valid_names": [
        'Kevin Welch',
        'Kim',
        'Smith',
        'Maria Delgado-Gonzalez',
        'ndiENAKdnw',
    ],
    "invalid_names": [
        'this.is.not.a.valid.name?',
        'invalid333',
        'n4m3',
    ],
    "parse_output": {
        'entries': [
            {'lastname': 'Smith', 'firstname': 'John', 'phonenumber': '623-668-9293', 'color': 'yellow', 'zipcode': '87360'}, 
            {'firstname': 'James', 'lastname': 'Murphy', 'color': 'yellow', 'zipcode': '83880', 'phonenumber': '018-154-6474'}, 
            {'firstname': 'Booker T.', 'lastname': 'Washington', 'zipcode': '87360', 'phonenumber': '373-781-7380', 'color': 'yellow'}
        ], 
        'errors': [3, 4, 5, 6, 7]
    }
}


