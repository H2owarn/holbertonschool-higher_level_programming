#!/usr/bin/python3
"""This module create a custom Python class named CustomObject"""


import pickle
import os


filename = "object.pkl"


class CustomObject:
    """person class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display information"""
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")


    def serialize(self, filename):
        """serialize the current instance of the object"""
        with open(filename, "wb") as file:
            pickle.dump(self, file)


    @classmethod
    def deserialize(cls, filename):
        """Deserialize from a file"""
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, "rb") as file:
                return pickle.load(file)
        else:
            return None
