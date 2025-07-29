#!/usr/bin/python3

with open('0-answer.txt') as t:
    function_name = t.read().strip()  # Reads and strips whitespace/newline
    obj = "Hello"  # Example object

    result = eval(f"{function_name}(obj)")
    print(result)

