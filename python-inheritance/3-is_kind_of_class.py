#!/usr/bin/python3
"""
    is_kind_of_class.
    """


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is class else return False.
        """
    if type(obj) is a_class:
        return True
    else:
        return False
