#!/usr/bin/python3
"""This module write a function that returns True if the object
    is exactly an instance of the specified class ; otherwise False."""  


def is_same_class(obj, a_class):
        """Return if obj is an instance of a_class"""
        return type(obj) is a_class
