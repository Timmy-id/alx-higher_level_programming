#!/usr/bin/python3
"""Create a LockedClass class"""


class LockedClass:
    """Prevent user from dynamically creating
        new instance attributes except for first_name
    """
    __slots__ = ['first_name']
