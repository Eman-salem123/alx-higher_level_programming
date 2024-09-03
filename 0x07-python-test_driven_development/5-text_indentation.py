#!/usr/bin/python3
""" Text indentation module """


def text_indentation(text):
    """  prints a text with 2 new lines after each of these characters: ., ? and : """
    if type(text) is not str:
        raise TypeError("text must be a string")
    x = 0
    while x < len(text):
        print(text[x], end="")
        if text[x] in ".?:":
            x += 1
            print("\n")
        x += 1
