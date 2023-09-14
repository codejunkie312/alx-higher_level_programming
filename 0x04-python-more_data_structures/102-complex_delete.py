#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    to_delete = []
    for k, v in a_dictionary.items():
        if value == v:
            to_delete.append(k)
    for element in to_delete:
        a_dictionary.pop(element)
    return a_dictionary
