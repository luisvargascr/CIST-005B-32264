"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/23/2024

Description: LinkedQueue
This file is used to represent a LinkedQueue object, and it is
a derived class from the Queue Abstract Class.
"""
from node import Node
from abstractqueue import AbstractQueue


class LinkedQueue(AbstractQueue):

    def __init__(self):
        self.__head = None
        self.__items = None
        self.__size = 0

    def __len__(self) -> int:
        """Returns the number of items in the queue. """
        return self.__size

    def __str__(self) -> str:
        """Returns the string representation of the queue. """
        if self.__size > 0:
            temp = self.__head
            output = []
            while temp:
                output.append(temp.value)
                temp = temp.next
            queue_output = output
            return str(queue_output)
        else:
            return "[]"

    def __iter__(self) -> object:
        """Returns an iterator to traverse through the elements
           in the queue. Visits each item in the queue from
           the front to the back. """
        temp = self.__head
        while temp:
            yield temp
            temp = temp.next

    def __contains__(self, item: object) -> bool:
        """Returns True if the queue contains the item being passed to it.
           Otherwise, it returns False. """
        current = self.__head
        while current and current.value != item:
            current = current.next

        if current:
            return True
        else:
            return False

    def __add__(self, other_queue: object) -> object:
        """Adds another queue to the front of
           the current queue and, as a result,
           returns a new queue. """
        if not self.__head:
            self.__head = other_queue.__head
            self.__items = other_queue.__items
            self.__size = other_queue.__size
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = other_queue.__head
        return self

    def __eq__(self, item: object) -> bool:
        """Compares two queues. Two queues are equal
           if the items at corresponding positions are
           equal. """
        if self.__size != item.__size:
            return False

        queue_a = self.__head
        queue_b = item.__head

        while queue_a and queue_b:
            if queue_a.value != queue_b.value:
                return False
            queue_a = queue_a.next
            queue_b = queue_b.next

        return True

    def isEmpty(self) -> bool:
        """Returns True if the queue is empty. False otherwise."""
        return self.__size == 0

    def clear(self) -> None:
        """Makes the queue become empty. """
        self.__head = None
        self.__items = None
        self.__size = 0

    def peek(self) -> object:
        """Returns the item at the beginning of the queue.
           Precondition: the queue must not be empty; raises
           a KeyError if the queue is empty. """
        if self.isEmpty():
            raise KeyError("Queue is empty!")
        return self.__head.value

    def enqueue(self, item: object) -> None:
        """Adds an item to the back of the queue. """
        current = None
        new_node = Node(item)
        if not self.__head:
            self.__head = new_node
        else:
            current = self.__head
            while current.next:
                current = current.next
            current.next = new_node
        self.__items = current
        self.__size += 1

    def dequeue(self) -> object:
        """Removes and returns the item at the front of
           the queue. Precondition: the queue must not be empty;
           raises a KeyError if the queue is empty."""
        if self.isEmpty():
            raise KeyError("Queue is empty!")

        first_item = self.__head.value
        self.__head = self.__head.next
        self.__size -= 1
        return first_item

    def size(self) -> int:
        """Returns the size of the queue. """
        return self.__size
