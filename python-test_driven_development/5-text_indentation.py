#!/usr/bin/python3
"""This module provides a function prints a text with 2 new lines after each of these characters: ., ? and : """


def text_indentation(text):
    """" 
    prints a text with 2 new lines.

    Args:
    text(str) : text must be a string.

    Raises:
    TypeError : if text is not string

    """
    if not isinstance(text, str):
        raise TypeError ("text must be a string")
    
    formatted_text = text.replace(",", ",\n\n").replace("?", "?\n\n").replace(":", ":\n\n")
    print(formatted_text)

