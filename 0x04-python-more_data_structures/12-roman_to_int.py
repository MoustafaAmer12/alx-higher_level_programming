#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if type(roman_string) is not str:
        return 0
    roman_int = 0
    tr = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for r_int in reversed(roman_string):
        roman_int += tr[r_int] if roman_int < tr[r_int] * 5 else -tr[r_int]
    return roman_int
