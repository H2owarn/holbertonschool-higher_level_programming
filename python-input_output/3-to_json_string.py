#!/usr/bin/python3
"""This module write a function return Json to string"""


import json
def to_json_string(my_obj):
    """Return the JSON reprentation of an object as a string"""
    return json.dumps(my_obj, ensure_ascii=False)
