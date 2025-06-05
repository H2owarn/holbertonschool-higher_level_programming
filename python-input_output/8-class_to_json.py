#!/usr/bin/python3
"""This module returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """Returns a dictionary description of an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("Object must have a __dict__ attributr")
    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (list, dict, str, int, bool))}
