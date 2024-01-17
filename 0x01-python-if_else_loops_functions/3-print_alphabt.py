#!/usr/bin/python3
"""Print all the letters in lowercase except q and e"""
for i in range(97, 123):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end="")
