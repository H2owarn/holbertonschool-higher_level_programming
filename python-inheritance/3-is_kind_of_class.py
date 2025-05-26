#!/usr/bin/python3
"""This module write a function that return True if the object is an
instance or the object is an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """Return True if the object is an instance of the class or inherited"""
    return isinstance(obj, a_class)
