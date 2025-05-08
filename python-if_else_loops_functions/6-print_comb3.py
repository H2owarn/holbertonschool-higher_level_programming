#!/usr/bin/python3
for i in range(1, 90):
    if i % 10 == 0:
        continue
    if i % 11 == 0:
        continue
    if i in [
        21, 31, 41, 51, 61, 71, 81, 32, 42, 52, 62, 72, 82, 43, 53, 63, 73, 83,
        54, 64, 74, 84, 65, 75, 85, 76, 86, 87
    ]:
        continue
    print("{}".format(f"{i:02d}"), end=", " if i != 89 else "\n")
