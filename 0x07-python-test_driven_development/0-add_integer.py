#!/usr/bin/python3

def add_integer(a, b=98):
    """
        Adds only integers or floats
    """
    if isinstance(a, float):
        a = int(a)
    
    if isinstance(b, float):
        b = int(b) 
    
    if isinstance(a, str) or isinstance(b, str):
        raise TypeError ('Both values must be numbers')
    
    if not(isinstance(a, (int, float))):
        raise TypeError ("a must be an integer")
    
    if not(isinstance(b, (int,float))):
        raise TypeError ("a must be an integer")
    
    return a+b
