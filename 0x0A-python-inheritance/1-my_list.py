#!/usr/bin/python3
    """a subclass of list"""

class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
