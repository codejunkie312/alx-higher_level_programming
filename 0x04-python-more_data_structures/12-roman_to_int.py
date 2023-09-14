#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_numerals = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    prev = 0
    for c in roman_string[::-1]:
        if roman_numerals[c] < prev:
            sum -= roman_numerals[c]
        else:
            sum += roman_numerals[c]
            prev = roman_numerals[c]
    return sum
