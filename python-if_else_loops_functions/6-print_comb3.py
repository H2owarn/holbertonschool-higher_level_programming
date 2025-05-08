#!/usr/bin/python3
for i in range(1,90):
    if i % 10 == 0:
        continue
    print("{}".format(f"{i:02d}"), end=", ")
