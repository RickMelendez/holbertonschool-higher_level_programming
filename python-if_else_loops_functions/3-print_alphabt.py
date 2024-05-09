#!/usr/bin/python3
for a in range(97, 123):
    if chr(a) != 101 and chr(a) != 113:
        print("{}".format(chr(a)), end="")