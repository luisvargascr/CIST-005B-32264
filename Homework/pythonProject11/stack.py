"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/23/2024

Description: Stack
This file is used to represent a Stack Abstract Class.
Concrete classes that use this class must implement the methods listed below.
"""

from abc import ABC, abstractmethod


class Stack(ABC):
    @abstractmethod
    def __len__(self) -> int:
        """Returns the number of items in the stack. """
        return 0

    @abstractmethod
    def __str__(self) -> str:
        """Returns the string representation of the stack. """
        return ""

    @abstractmethod
    def __iter__(self) -> object:
        """Returns an iterator to traverse through the elements
           in the stack. Visits each item in the stack from
           bottom to top. """
        return None

    @abstractmethod
    def __contains__(self, item: object) -> bool:
        """Returns True if the stack contains the item being passed to it.
           Otherwise, it returns False. """
        return False

    @abstractmethod
    def __add__(self, item: object) -> None:
        """Adds another stack on the top of
           the current stack and, as a result,
           returns a new stack. """
        pass

    @abstractmethod
    def __eq__(self, item: object) -> bool:
        """Compares two stacks. Two stacks are equal
           if the items at corresponding positions are
           equal. """
        return False

    @abstractmethod
    def isEmpty(self) -> bool:
        """Returns True if the stack is empty. False otherwise."""
        return True

    @abstractmethod
    def clear(self) -> None:
        """Makes the stack become empty. """
        pass

    @abstractmethod
    def peek(self) -> object:
        """Returns the item at the top of the stack.
           Precondition: the stack must not be empty; raises
           a KeyError if the stack is empty. """
        return None

    @abstractmethod
    def push(self, item: object) -> None:
        """Adds an item to the top of the stack. """
        pass

    @abstractmethod
    def pop(self) -> object:
        """Removes and returns the item at the top of
           the stack. Precondition: the stack must not be empty;
           raises a KeyError if the stack is empty."""
        return None
