#!/usr/bin/python3
"""This module writr the function that write content in to the file"""


def write_file(filename="", text=""):
    """write a text file and return lenth of characters"""
    with open(filename, 'w', encoding="utf-8") as file:
        write_content = file.write(text)
        return write_content
