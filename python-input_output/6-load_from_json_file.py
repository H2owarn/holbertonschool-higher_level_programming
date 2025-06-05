#!/usr/bin/python3
"""This module write a function that creates an Object from a “JSON file"""


import json


def load_from_json_file(filename):
    """Creat an object from a JSON file"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
