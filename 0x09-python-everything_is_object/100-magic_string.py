#!/usr/bin/python3
def magic_string():
    setattr(magic_string, 'rep', getattr(magic_string, 'rep', -1) + 1)
    return "Best School" + ", Best School" * getattr(magic_string, 'rep', 0)
