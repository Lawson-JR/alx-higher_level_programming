#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Represent a square."""
        """
            Args:
                size (int): The size of the new Square.
                x (int): The x coordinate of the new Square.
                y (int): The y coordinate of the new Square.
                id (int): The identity of the new Square.
        """
        super.__init__(id, x, y, width, height)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
