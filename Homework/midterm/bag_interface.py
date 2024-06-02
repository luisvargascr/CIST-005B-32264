"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: BagInterface
This file is used to represent an Interface for a Bag Data Structure
"""


class BagInterface(object):
    """Interface to represent a Bag Data Structure."""

    def __init__(self, source_collection: object = None):
        """Constructor to be implemented in the Concrete Class Implementing the Interface."""
        pass

    def isEmpty(self):
        """Returns True if the Bag is empty; otherwise, False."""
        return True

    def __len__(self):
        """Returns the number of items in the Bag."""
        return 0

    def __str__(self):
        """Returns the string representation of the Bag."""
        return ""

    def __iter__(self):
        """Returns the iterator of the Bag."""
        return None

    def __add__(self, other):
        """Adds an element to the Bag."""
        return None

    def __eq__(self, other):
        """Compares an element with elements already in the Bag."""
        return False

    def count(self, item):
        """Returns the count of elements already in the Bag."""
        return 0

    def clear(self):
        """Clears the items in the Bag."""
        pass

    def add(self, item):
        """Adds element to the Bag."""
        pass

    def remove(self, item):
        """Removes element from the Bag."""
        pass
