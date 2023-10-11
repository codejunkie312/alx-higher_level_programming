#!/usr/bin/python3
"""A module that contains a script that reads stdin line by line and
computes metrics.
"""
import sys


total_size = 0
status_code_counts = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
    }
line_count = 0


def print_stats(file_size, status_code_counts):
    """Prints the computed metrics to stdout.

    Args:
        file_size (int): The total file size.
        status_code_counts (dict): A dictionary containing the status
        codes and their counts.
    """
    print("File size: {:d}".format(file_size))
    for key in sorted(status_code_counts.keys()):
        if status_code_counts[key] != 0:
            print("{:s}: {:d}".format(key, status_code_counts[key]))


try:
    for line in sys.stdin:
        try:
            line_count += 1
            split_line = line.split()
            total_size += int(split_line[-1])
            status_code = split_line[-2]
            if status_code in status_code_counts.keys():
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1
            if line_count % 10 == 0:
                print_stats(total_size, status_code_counts)
        except Exception:
            continue
except KeyboardInterrupt:
    print_stats(total_size, status_code_counts)
    raise
