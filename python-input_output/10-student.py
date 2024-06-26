#!/usr/bin/python3
"""Student module
"""


class Student:
    """Contains student data
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary of Student with conditions to filter
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            temp = {}
            for elem in attrs:
                if not isinstance(elem, str):
                    return self.__dict__
                if elem in self.__dict__:
                    temp[elem] = self.__dict__[elem]
            return temp
