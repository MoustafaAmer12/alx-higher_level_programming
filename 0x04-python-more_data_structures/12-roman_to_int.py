#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if type(roman_string) is not str:
        return 0
    roman_int = 0
    for i in range(len(roman_string)):
        if roman_string[i] == "V":
            if i+1 < len(roman_string):
                if roman_string[i+1] == "D" or roman_string[i+1] == "L" or\
                        roman_string[i+1] == "M":
                    roman_int -= 5
                else:
                    roman_int += 5
            else:
                roman_int += 5
        elif roman_string[i] == "X":
            if i+1 < len(roman_string):
                if roman_string[i+1] == "D" or roman_string[i+1] == "L" or\
                        roman_string[i+1] == "M":
                    roman_int -= 10
                else:
                    roman_int += 10
            else:
                roman_int += 10
        elif roman_string[i] == "L":
            if i+1 < len(roman_string):
                if roman_string[i+1] == "D" or roman_string[i+1] == "M":
                    roman_int -= 50
                else:
                    roman_int += 50
            else:
                roman_int += 50
        elif roman_string[i] == "C":
            if i+1 < len(roman_string):
                if roman_string[i+1] == "D" or roman_string[i+1] == "M":
                    roman_int -= 100
                else:
                    roman_int += 100
            else:
                roman_int += 100
        elif roman_string[i] == "D":
            roman_int += 500
        elif roman_string[i] == "M":
            roman_int += 1000
        elif roman_string[i] == "I":
            if i+1 < len(roman_string):
                if roman_string[i+1] == "I":
                    roman_int += 1
                else:
                    roman_int -= 1
            else:
                roman_int += 1
    return roman_int
