#!/usr/bin/python3
"""This module write a function that returns the list."""

def lookup(obj):
    """Return a list of available attributes and methods of an object"""
    return dir(obj)
