#!/usr/bin/python3
"""This module write a class Student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the json with only specific attribute"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr, None) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
