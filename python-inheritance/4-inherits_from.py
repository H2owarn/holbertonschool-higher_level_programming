#!/usr/bin/python3
"""This module write function check if the object’s class 
is a subclass (meaning it was built on top of another class) of a given 
class—but it returns True only if the instance’s type is different 
from the class itself. 
"""


def inherits_from(obj, a_class):
    """Return True if the object is an instance of a class that inherited 
    (directly or indirectly) from the specified class"""
    return type(obj) is not a_class and issubclass(type(obj), a_class)
