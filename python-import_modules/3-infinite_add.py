#!/usr/bin/python3
import sys


def main():

    numbers = sys.argv[1:]
    if len(numbers) == 0:
        print("0")
    else:
        total = sum(int(num) for num in numbers)
        print(total)


if __name__ == "__main__":
    main()
