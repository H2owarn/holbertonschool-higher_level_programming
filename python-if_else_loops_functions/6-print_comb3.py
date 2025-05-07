#!/usr/bin/python3
for i in range(1,100):
    if i % 10 == 0:
        continue
    print(f"{i:02d}, ", end="")
