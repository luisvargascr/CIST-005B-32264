"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 02/25/2024

Description: For this exercise:

1) Write an ArrayBag class and fill it out
   with 6,-1,8,5,85,-12.
2) Check if the ArrayBag is empty.
3) Remove the number 5 from the ArrayBag
4) Print the content of the ArrayBag
5) In the end, make the ArrayBag empty
6) Check if the ArrayBag is empty

"""
from bag_interface import BagInterface
from arrays import Array


class ArrayBag(BagInterface):
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        super().__init__()
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __len__(self):
        return self.size

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __str__(self):
        return "{" + ",".join(map(str, self)) + "}"

    def __add__(self, other):
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other) or \
                len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False

        return True

    def isEmpty(self) -> bool:
        return len(self) == 0

    def count(self, item) -> int:
        return len(self)

    def clear(self) -> None:
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item) -> None:
        self.items[len(self)] = item
        self.size += 1

    def remove(self, item) -> None:
        if not item in self:
            raise KeyError(str(item) + " is not in the bag!")
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1

        for i in range(targetIndex, len(self) - 1):
            self.items[i] = self.items[i + 1]
        self.size -= 1


if __name__ == '__main__':

    my_bag = ArrayBag()
    my_bag.add(6)
    my_bag.add(-1)
    my_bag.add(8)
    my_bag.add(5)
    my_bag.add(85)
    my_bag.add(-12)

    print("The content of the ArrayBag is now: '%s'." % (my_bag))
    print("Is the ArrayBag empty? %s." % (my_bag.isEmpty()))
    print("Remove item 5...")
    my_bag.remove(5)
    print("The content of the ArrayBag after removing the item is: '%s'." % (my_bag))
    my_bag.clear()
    print("The ArrayBag was cleared out.")
    print("Is the ArrayBag empty? %s." % (my_bag.isEmpty()))