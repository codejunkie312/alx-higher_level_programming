#!/usr/bin/python3
def uppercase(str):
    token = ""
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            token += chr(ord(c) - 32)
        else:
            token += c
    print("{}".format(token))
