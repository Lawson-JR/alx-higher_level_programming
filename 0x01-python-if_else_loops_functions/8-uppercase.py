#!/usr/bin/python3
def convert_to_uppercase(string):
    uppercase_chars = []

    for char in string:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            uppercase_chars.append(uppercase_char)
        else:
            uppercase_chars.append(char)

    return ''.join(uppercase_chars)
