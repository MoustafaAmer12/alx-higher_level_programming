#!/usr/bin/python3
"""
Module that translates a text into another format
text_indentation:
    formats text to 2 new lines after special chars
"""


def text_indentation(text):
    """Prints the new translated text
    Returns:
        None"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    new = False
    for ch in text:
        if new and ch == " ":
            continue
        new = False
        print(ch, end="")
        if ch in ".?:":
            print("\n")
            new = True
