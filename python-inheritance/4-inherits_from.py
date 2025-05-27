#!/usr/bin/python3
"""This module write function check if the object’s class 
is a subclass"""


def inherits_from(obj, a_class):
    """Return True if the object is an instance of a class that inherited 
    (directly or indirectly)"""
    return type(obj) is not a_class and issubclass(type(obj), a_class)
