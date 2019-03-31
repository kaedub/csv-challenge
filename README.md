# Corax Interivew Challenge - Python

This program will parse a file containing entries of personal information in a variety of formats, sort the entries and record invalid lines, then write the results as valid JSON indented two spaces to `result.json` file. The keys for each entry are sorted alphabetically and the entries are sorted alphabetically by last name then first name.

It can easily handle a file up with a few hundred thousand lines but does not yet implement external sorting, so very large file sizes will consume too much memory.

_Where this program shines is in extensibility._  

New formats and field types can be added very easily. More details on how to do this below.

## How to run the program from the command line

_Written in Python 3.7.0 using only the Python standard library, no package installation is necessary._

`python3 app.py`

This will create a file called `result.json` containing the sorted entries and errors.

## How to add new formats

__Adding formats__

New formats can be added to the `formats.csv` file as long as they are allowed fields.

*Example of how to add a fourth pattern to `formats.csv`:*  

```
lastname,firstname,phone_hyphenated,color,zipcode
fullname,color,zipcode,phone_spaced
firstname,lastname,zipcode,phone_spaced,color
color,zipcode,fullname,phone_spaced
```

If you use a field that has not been added to the valiation such `age`, the program will throw an informative error. See next section on how to add new fields.


_NOTE: It is important to know that in the program's current state, all formats must contain a `firstname` and `lastname` field or a `fullname` field so the results can be sorted._

__Adding new fields__

You can easily add new fields with only a few lines of code. 

This allows formats to use new fields, such as "age", "middle name", or anything else you may need.  

To add a new field, simple add the field name and a validator function to the `field_validators` object in `validation.py`. Each field needs a validator function for that field name. You may use existing validators or create your own.

*Here is how you can add an "age" and "middlename" field to use in your formats:*

```
"""validation.py"""

def is_age(n):
	return 0 n < 200

field_validators = {
    "lastname": is_name,
    "firstname": is_name,
    ...,
    "zipcode": is_zip,
    "age": is_age,          # age uses a new validator function
    "middlename": is_name   # middlename can use an existing validator, "is_name"
}
```

By setting a field name as key and a validator function as the value in the `field_validators` dictionary, you can customize how you validate each field.


_NOTE: It is important to know that complex fields require some editing. A compound field such as `fullname` must be split into a `firstname` and `lastname` field before being sorted and written to the JSON file. This is similar for phone numbers, which have 2 different field types for the two phone number formats but both msut be considered a `phonenumber` field before being sorted and written. Take a look at the `Parser._parse_field()` method if you wish to do this._


## If I had more time...

1) I would like to implement **external sorting** for large files. This will increase the time it takes to run the program but would allow for extremely large file sizes. This would require some refactoring in the Parser class to allow data to be fed in parts so it can be sorted in chunks that fit in RAM and then merged later when writing to the JSON file.

2) I would like spend some time **minimizing format dependecies for the Parser** by adding a means of programmatically enforcing common fields across formats. This could be done by making format validation more robust by setting a list of required fields for formats that can be used by the Parser to sort.

3) I would like to spend more time **separating concerns**. The logic to write to a json file can be separated out to a reusable means of generating JSON by accepting data as an ordered dictionary. Also, sorting could be separated out so that different methods of sorting can be used depending on input size.