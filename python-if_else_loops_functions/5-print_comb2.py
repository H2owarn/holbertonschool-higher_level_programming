#!/usr/bin/python3
for i in range(0, 100):
    print("{}".format(f"{i:02d}"), end=", " if i < 99 else "\n")
