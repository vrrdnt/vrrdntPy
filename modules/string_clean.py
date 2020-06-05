"""
This takes in a string and adds \ to any illegal characters so it can be
uploaded to YouTube through the uploader.

Code originally appeared at https://github.com/RustyRin/Music2Video/blob/master/working/string_clean.py
"""

illegal = ['<', '>', '/', '\\', '\'', '\"']


def clean(string):
    for c in string:
        if c in illegal:
            string = string.replace(c, '')

    return string
