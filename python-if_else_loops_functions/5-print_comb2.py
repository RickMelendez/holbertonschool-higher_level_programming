#!/usr/bin/python3
for t in range(100):
    if t < 99:
        print("{:2d}, ".format(t), end="")
    else:
        print(t)
