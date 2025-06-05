#!/usr/bin/python3
"""This module create a serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file"""
    with open(filename, 'w',) as file:
        json.dump(data,file)
    pass

def load_and_deserialize(filename):
    """Deserialize a JSON file to recreate the Python dictionary."""
    with open(filename, 'r') as file:
        data = json.load(file)
        return data
    pass
