#!/usr/bin/python3

if __name__ == "__main__":
    """prints the result of the addition of all arguments"""
    import sys

    sum = 0

    for i in range(len(sys.argv) - 1):
        sum = sum + int(sys.argv[i + 1])
    print("{}".format(sum))
