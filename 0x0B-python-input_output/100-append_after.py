#!/usr/bin/python3
"""Module that defines a function
to append a text after each occurrence of
a pattern in a file
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        idx = 0
        for line in lines:
            if line.find(search_string) != -1:
                new_line = line + new_string
                lines[idx] = new_line
            idx += 1
        file.seek(0)
        for line in lines:
            file.writelines(line)
