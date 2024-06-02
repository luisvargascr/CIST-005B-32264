"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: This Class represents a linked list implementation
of the BagInterface.
"""

from bag_interface import BagInterface
from node import Node


class LinkedBag(BagInterface):
    """Concrete class that represents a Linked Bag Object."""

    def __init__(self, sourceCollection=None):
        """Constructor"""
        super().__init__()
        self.items = None
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __iter__(self):
        """Returns the iterator for the Linked Bag Object."""
        cursor = self.items
        while cursor is not None:
            yield cursor.value
            cursor = cursor.next

    def __str__(self):
        """Returns the string representation of the Linked Bag Object."""
        return "{" + ",".join(map(str, self)) + "}"

    def __len__(self):
        """Returns the number of items (length) of the Linked Bag Object."""
        return self.items

    def __add__(self, other):
        """Adds a new item to the Linked Bag Object."""
        cursor = self.items
        while cursor:
            cursor = cursor.next
        cursor.next = other
        self.size += 1

    def __eq__(self, other):
        """Compares an item to the items in the Linked Bag Object."""
        if self is other: return True
        if type(self) != type(other) or \
                len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False

    def count(self, item) -> int:
        """Counts the number of items in the Linked Bag Object."""
        return self.size

    def find(self, item: str) -> Node | None:
        """Attempts to find a specific item in the Linked Bag Object and if found returns it; otherwise
           returns None."""
        cursor = self.items
        tmp = None
        while cursor:
            if cursor.value.name == item:
                tmp = cursor
            cursor = cursor.next
        return tmp

    def isEmpty(self) -> bool:
        """Checks if the Linked Bag Object is empty."""
        return self.size == 0

    def add(self, item) -> None:
        """Adds a new item to the Linked Bag Object."""
        new_node = Node(item)
        if not self.items:
            self.items = new_node
        else:
            tmp = self.items
            while tmp.next:
                tmp = tmp.next
            tmp.next = new_node

        self.size += 1

    def clear(self) -> None:
        """Clears / Removes ALL items in the Linked Bag Object."""
        self.items = None
        self.size = 0

    def remove(self, item) -> None:
        """Removes a specific item from the Linked Bag Object."""
        if item.value not in self:
            raise KeyError(str(item.value.name) + " is not in the bag!")
        probe = self.items
        trailer = None

        for targetItem in self:
            if targetItem == item.value:
                break
            trailer = probe
            probe = probe.next

        if probe == self.items:
            self.items = self.items.next
        else:
            trailer.next = probe.next

        self.size -= 1
