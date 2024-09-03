#!/usr/bin/python3
""" square print module """


def print_square(size):
    """  prints a square with the character # """
    if type(size) is int:
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            for a in range(size):
                print("".join("#" for z in range(size)))
    else:
        raise TypeError("size must be an integer")
