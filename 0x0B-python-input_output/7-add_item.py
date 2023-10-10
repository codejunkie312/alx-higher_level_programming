#!/usr/bin/python3
"""
This script adds arguments passed to it to a list and saves
the list to a JSON file.
If the file already exists, it loads the existing list from the
file and appends the new arguments to it.
If the file does not exist, it creates an empty list and appends
the new arguments to it.
The resulting list is then saved to the file in JSON format.
"""
import sys
from os import path
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, filename)
