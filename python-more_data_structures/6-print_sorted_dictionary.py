#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dic = dict(sorted(a_dictionary.items()))
    for key, value in sort_dic.items():
        print(f"{key}: {value}")
