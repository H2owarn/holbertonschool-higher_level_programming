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

    i = 0
    while i < len(text):
        print(text[i], end="")

        if text[i] in ['.', '?', ':', ',']:
            print("\n")
            i += 1

            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
