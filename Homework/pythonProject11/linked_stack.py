"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/23/2024

Description: LinkedStack
This file is used to represent a LinkedStack object, and it is
a derived class from the Stack Abstract Class.
"""
from node import Node
from stack import Stack


class LinkedStack(Stack):

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__items = None
        self.__size = 0

    def __len__(self) -> int:
        """Returns the number of items in the stack. """
        return self.__size

    def __str__(self) -> str:
        """Returns the string representation of the stack. """
        if self.__size > 0:
            temp = self.__head
            output = []
            while temp:
                output.append(temp.value)
                temp = temp.next
            return str(output)
        else:
            return "[]"

    def __iter__(self) -> object:
        """Returns an iterator to traverse through the elements
           in the stack. Visits each item in the stack from
           bottom to top. """
        temp = self.__head
        while temp:
            yield temp
            temp = temp.next

    def __contains__(self, item: object) -> bool:
        """Returns True if the stack contains the item being passed to it.
           Otherwise, it returns False. """
        current = self.__head
        while current and current.value != item:
            current = current.next

        if current:
            return True
        else:
            return False

    def __add__(self, other_stack: object) -> object:
        """Adds another stack on the top of
           the current stack and, as a result,
           returns a new stack. """
        if not self.__head and not self.__tail:
            self.__tail = other_stack.__tail
            self.__head = other_stack.__head
            self.__items = other_stack.__items
            self.__size = other_stack.__size
        else:
            self.__tail.next = other_stack.__head
            self.__tail = other_stack.__tail
            self.__size += other_stack.__size
        return self

    def __eq__(self, item: object) -> bool:
        """Compares two stacks. Two stacks are equal
           if the items at corresponding positions are
           equal. """
        if self.__size != item.__size:
            return False

        stack_a = self.__head
        stack_b = item.__head

        while stack_a and stack_b:
            if stack_a.value != stack_b.value:
                return False
            stack_a = stack_a.next
            stack_b = stack_b.next

        return True

    def isEmpty(self) -> bool:
        """Returns True if the stack is empty. False otherwise."""
        return self.__size == 0

    def clear(self) -> None:
        """Makes the stack become empty. """
        self.__head = None
        self.__tail = None
        self.__items = None
        self.__size = 0

    def peek(self) -> object:
        """Returns the item at the top of the stack.
           Precondition: the stack must not be empty; raises
           a KeyError if the stack is empty. """
        if self.isEmpty():
            raise KeyError("Stack is empty!")
        return self.__tail.value

    def push(self, item: object) -> None:
        """Adds an item to the top of the stack. """
        if not self.__head:
            self.__head = Node(item, None)
            self.__tail = self.__head
        else:
            current = self.__tail
            current.next = Node(item, None)
            self.__tail = current.next
        self.__items = self.__head
        self.__size += 1

    def pop(self) -> object:
        """Removes and returns the item at the top of
           the stack. Precondition: the stack must not be empty;
           raises a KeyError if the stack is empty."""
        if self.isEmpty():
            raise KeyError("Stack is empty!")

        last_item = self.__tail.value
        current = self.__head
        second_to_last = None

        if current:
            while current:
                if current.next:
                    second_to_last = current
                current = current.next

            if second_to_last:
                second_to_last.next = None

        if self.__tail == self.__head:
            self.__head = second_to_last
        self.__tail = second_to_last
        self.__size -= 1
        return last_item

    def size(self) -> int:
        """Returns the size of the stack. """
        return self.__size
