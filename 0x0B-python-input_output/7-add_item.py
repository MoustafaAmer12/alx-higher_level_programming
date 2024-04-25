#!/usr/bin/python3
"""
A Module that takes arguments and keeps
adding them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    des_list = load_from_json_file(filename)
except Exception:
    des_list = []

for item in sys.argv[1:]:
    des_list.append(item)
save_to_json_file(des_list, filename)
