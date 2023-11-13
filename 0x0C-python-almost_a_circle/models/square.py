#!/usr/bin/python3
"""
new class square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    new class square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        init
        """
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y
        self.id = id

    def __str__(self):
        """
        str
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """
        size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
