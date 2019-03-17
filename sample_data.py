test_case_data = {
    "valid_phones": [
        '703 742 0996',
        '646 111 0101',
        '703 955 0373',
        '(703)-742-0996',
        '(646)-111-0101',
        '(703)-955-0373',
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
        'ndiENAKdnw',
    ],
    "invalid_names": [
        'this-is-not-a-valid-name',
        'this may be a valid name',
        'invalid333',
        'n4m3',
    ]
}


