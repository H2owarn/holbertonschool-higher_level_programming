#!/usr/bin/python3
"""This module write a class MyList that inherits from list."""


class MyList(list):
    """Return class MyList that inherits from list."""
    def print_sorted(self):
        print (sorted(self))
