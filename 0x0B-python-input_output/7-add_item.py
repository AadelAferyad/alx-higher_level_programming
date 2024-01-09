#!/usr/bin/python3
""" file.json """
import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
st = []
i = 1
if os.path.exists(filename):
    st = load_from_json_file(filename)

while i < len(sys.argv):
    st.append(sys.argv[i])
    i += 1

save_to_json_file(st, filename)
