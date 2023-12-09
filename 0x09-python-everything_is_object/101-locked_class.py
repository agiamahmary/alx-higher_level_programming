#!/usr/bin/python3
"""Contains locked class """


class LockedClass:
    """Contains only one public instance attr """

    __slots__ = ["first_name"]

    def __init__(self):
        self.first_name = "first_name"
