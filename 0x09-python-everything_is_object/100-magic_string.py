#!/usr/bin/python3
def magic_string():
    setattr(magic_string, 'rep', getattr(magic_string, 'rep', -1) + 1)
    return "BestSchool" + ", BestSchool" * getattr(magic_string, 'rep', 0)
