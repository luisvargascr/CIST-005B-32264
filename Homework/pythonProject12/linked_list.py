"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/31/2024

Description: LinkedList
This file is used to represent a LinkedList object, and it is
a derived class from the Abstract List Class.
"""
from abstract_list import AbstractList
from node import Node


class LinkedList(AbstractList):

    def __init__(self):
        self.__head = None
        self.size = 0

    def __iter__(self):
        cursor = self.__head.next
        while cursor != self.__head:
            yield cursor.data
            cursor = cursor.next

    def __getitem__(self, index: int) -> object:
        if index < 0 or index >= len(self):
            raise IndexError("List index out of range")
        return self._get_item_based_on_index(index).data

    def __setitem__(self, index: int, value: object):
        if index < 0 or index >= len(self):
            raise IndexError("List index out of range")
        self._get_item_based_on_index(index).data = value

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        content = []
        current = self.__head
        while current:
            content.append(current.data)
            current = current.next
        return str(content)

    def is_empty(self) -> bool:
        return self.size == 0

    def clear(self) -> None:
        self.size = 0
        self.__head = None

    def Insert(self, index: int, item: object) -> None:
        """Inserts the item at position index."""
        if index < 0:
            index = 0
        elif index > len(self):
            index = len(self) - 1

        new_node = Node(item)

        if not self.__head:
            self.__head = new_node
        else:
            current = self.__head
            previous = None
            current_index = 0

            if index == 0:
                while current.next:
                    current = current.next
                current.next = new_node

            else:
                while current.next and index != current_index:
                    previous = current
                    current = current.next
                previous.next = new_node
                new_node.next = current

        self.size += 1

    def Pop(self, index: int = None) -> object:
        if index is None:
            index = len(self) - 1
        if index < 0 or index >= len(self):
            raise IndexError("List index out of range")
        item = None

        if index == 0:
            item = self.__head.data
            self.__head = self.__head.next
        else:
            current = self.__head
            previous = self.__head
            current_index = 0

            while current:
                if current_index == index:
                    item = current.data
                    break
                previous = current
                current = current.next
                current_index += 1

            previous.next = current.next
            self.size -= 1

        return item

    def add(self, item: object) -> object:
        self.Insert(0, item)
        return self.__head

    def remove(self, item: object) -> None:
        index_item = self._get_index_based_on_item(item)
        if index_item >= 0:
            self.Pop(index_item)
        else:
            raise IndexError("List index out of range")

    def _get_item_based_on_index(self, index: int) -> object:
        current_index = 0
        current = self.__head
        while current:
            if current_index == index:
                return current
            current = current.next
            current_index += 1
        return None

    def _get_index_based_on_item(self, item: object) -> int:
        current_index = 0
        current = self.__head
        while current:
            if current.data == item:
                return current_index
            current = current.next
            current_index += 1
        return -1
