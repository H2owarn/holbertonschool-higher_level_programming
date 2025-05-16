#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    best_s = float('-inf') ## smallest posible number
 
    for key, value in a_dictionary.items():
        if value > best_s:
            best_s = value
            best_key = key
    return (best_key)
