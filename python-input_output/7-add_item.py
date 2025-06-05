#!/usr/bin/python3
"""This module write a script that adds all arguments to a Python list"""


import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

def main():
    """Adds argument to a list and save to JSON file"""
    try:
        if os.path.exists(filename):
            my_list = load_from_json_file(filename)
        else:
            my_list = []

        my_list.extend(sys.argv[1:])  # Exclude script name from arguments

        save_to_json_file(my_list, filename)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
