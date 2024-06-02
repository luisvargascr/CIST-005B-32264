"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 02/17/2024

Description: This program solves Chapter 4 Exercise 1:
Write an Array Data Structure which has a constructor,
"len", "str", "iter", "getitem" and "setitem" methods.
Then create an object of this Array class with 6 elements
in it. Fill the object of this class with numbers from 3 to 8.

print the array and show the length of the array object.
"""


class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem


if __name__ == '__main__':
    myArray = Array(6)
    i = 0
    for i, num in enumerate(range(3, 9, 1)):
        myArray.__setitem__(i, num)

    print("\nThe array is %s." % myArray)
    print("The length of the array is %s." % myArray.__len__())