#!/usr/bin/python3

def text_indentation(text):
    if not(isinstance(text, str)):
        raise TypeError ('text must be a string')
    
    result = ""
    punctuation_marks = ['.', ':', '?']
    for chars in text:
        result += chars
        if chars in punctuation_marks:
            result += '\n\n'
    print(result.strip())
