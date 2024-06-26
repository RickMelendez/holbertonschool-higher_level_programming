#!/usr/bin/python3
"""
    inherits_from.
    """


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class; else False.
        """

    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
