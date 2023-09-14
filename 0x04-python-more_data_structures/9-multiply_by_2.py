#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    return {key: value * 2 for key, value in new_dict.items()}
