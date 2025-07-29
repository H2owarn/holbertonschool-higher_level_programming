#!/usr/bin/python3

with open('1-answer.txt') as t:
    function_name = t.read().strip()  # Reads and strips whitespace/newline
    obj = [1, 2, 3]  # Example object

    result = eval(f"{function_name}(obj)")
    print(result)

