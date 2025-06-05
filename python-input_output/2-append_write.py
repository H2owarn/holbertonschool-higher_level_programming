#!/usr/bin/python3
"""This module write a function append strint to text file """


def append_write(filename="", text=""):
    """append a string to the end of a text file"""
    with open(filename, 'a', encoding="utf-8") as file:
        append_lenth = file.write(text)
        return append_lenth
