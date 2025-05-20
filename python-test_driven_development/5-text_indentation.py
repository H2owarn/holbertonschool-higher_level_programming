#!/usr/bin/python3
"""
This module provides a function
prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """"
    prints a text with 2 new lines.

    Args:
    text(str) : text must be a string.

    Raises:
    TypeError : if text is not string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for i, char in enumerate(text):
        if char in ".?:":
            sentence = text[start:i + 1].strip()
            print(sentence)
            print()
            start = i + 1
        
    if start < len(text):
        trailing = text[start:].strip()
        if trailing:
            print(trailing, end="")