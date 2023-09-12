#!/usr/bin/python3
def no_c(my_string):
    temp = ""
    for c in my_string:
        if c in "cC":
            continue
        temp += c
    return temp
