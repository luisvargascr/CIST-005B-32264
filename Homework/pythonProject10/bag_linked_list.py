"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 02/25/2024

Description: For this exercise:

1) Write a LinkedBag class and fill it out
with 6,-1,8,5,85, -12.
2) Check if the LinkedBag is empty.
3) Remove the number 5 from the LinkedBag
4) Print the content of the LinkedBag
5) In the end, make the LinkedBag empty
Check if the LinkedBag is empty

"""

from bag_interface import BagInterface
from node import Node


class LinkedBag(BagInterface):
    def __init__(self, sourceCollection=None):
        super().__init__()
        self.items = None
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __iter__(self):
        cursor = self.items
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return "{" + ",".join(map(str, self)) + "}"

    def __len__(self):
        return self.items

    def __add__(self, other):
        cursor = self.items
        while cursor:
            cursor = cursor.next
        cursor.next = other
        self.size += 1

    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other) or \
                len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False

    def count(self, item) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

    def add(self, item) -> None:
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
        self.items = None
        self.size = 0

    def remove(self, item) -> None:
        if not item in self:
            raise KeyError(str(item) + " is not in the bag!")
        probe = self.items
        trailer = None

        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next

        if probe == self.items:
            self.items = self.items.next
        else:
            trailer.next = probe.next

        self.size -= 1


if __name__ == "__main__":
    nums = [6, -1, 8, 5, 85, -12]
    linked_bag = LinkedBag(nums)
    print("The content of the LinkedBag is now: '%s'." % (linked_bag))
    print("Is the LinkedBag empty? %s." % (linked_bag.isEmpty()))
    print("Remove item 5...")
    linked_bag.remove(5)
    print("The content of the LinkedBag after removing the item is: '%s'." % (linked_bag))
    linked_bag.clear()
    print("The LinkedBag was cleared out.")
    print("Is the LinkedBag empty? %s." % (linked_bag.isEmpty()))

