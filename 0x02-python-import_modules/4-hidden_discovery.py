#!/usr/bin/python3
import importlib

hidden_4 = importlib.import_module("hidden_4")

if __name__ == "__main__":
    for i in dir(hidden_4):
        if not i.startswith("__"):
            print(i)
