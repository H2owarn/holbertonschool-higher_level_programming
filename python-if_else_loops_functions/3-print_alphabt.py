#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end="")

# The code prints the letters of the alphabet from 'a' to 'z', excluding 'q' and 'e'.        