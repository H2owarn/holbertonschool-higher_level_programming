#!/usr/bin/python3
def uppercase(str):
    """Converts a string to uppercase.

    Args:
        str (str): The string to convert.

    Returns:
        str: The uppercase version of the input string.
    """
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
