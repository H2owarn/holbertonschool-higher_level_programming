def say_my_name(first_name, last_name):
    """
    Prints "My name is <first name> <last name>"

    Args:
        first_name: str
        last_name: str

    Raises:
        TypeError: if either name is not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {}{}".format(first_name, f" {last_name}" if last_name else ""))
