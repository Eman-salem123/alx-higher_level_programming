#!/usr/bin/python3
""" 1-my_list module """


class MyList(list):
    """Mylist class"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """print_sorted function thats print lists in sorted form 0 to more"""
        print(sorted(self))
