#!/usr/bin/python3
import sys
def main():


    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print(f"{len(arguments)} arguments.")
    elif len(arguments) == 1:
        print(f"{len(arguments)} argument:")
    else:
        print(f"{len(arguments)} arguments:")
    for i, arg in enumerate(arguments, start=1):
        print(f"{i}: {arg}")


if __name__ == "__main__":

    main()
