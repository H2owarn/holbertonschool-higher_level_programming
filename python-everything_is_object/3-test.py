#!/usr/bin/python3

with open('2-answer.txt') as t:
    function_name = t.read().strip()  # Reads and strips whitespace/newline
    obja = 100  # Example object
    objb = 100  # Example object


    result = eval(f"(obja){function_name}(objb)")
    print(result)

