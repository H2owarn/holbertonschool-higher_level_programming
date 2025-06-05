#!/usr/bin/python3
"""This module writr a function resd text file """


def read_file(filename=""):
    """read a text file and print its content as a string"""
    with open(filename, 'r', encoding="utf-8" ) as file:
        content = file.read()
        print(content)