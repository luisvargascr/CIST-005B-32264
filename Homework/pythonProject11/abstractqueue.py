"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/23/2024

Description: AbstractQueue
This file is used to represent a Queue Abstract Class.
Concrete classes that use this class must implement the methods listed below.
"""

from abc import ABC, abstractmethod


class AbstractQueue(ABC):
    @abstractmethod
    def __len__(self) -> int:
        """Returns the number of items in the queue. """
        return 0

    @abstractmethod
    def __str__(self) -> str:
        """Returns the string representation of the queue. """
        return ""

    @abstractmethod
    def __iter__(self) -> object:
        """Returns an iterator to traverse through the elements
           in the queue. Visits each item in the queue from
           the front to the back. """
        return None

    @abstractmethod
    def __contains__(self, item: object) -> bool:
        """Returns True if the queue contains the item being passed to it.
           Otherwise, it returns False. """
        return False

    @abstractmethod
    def __add__(self, item: object) -> None:
        """Adds another queue to the front of
           the current queue and, as a result,
           returns a new queue. """
        pass

    @abstractmethod
    def __eq__(self, item: object) -> bool:
        """Compares two queue. Two queues are equal
           if the items at corresponding positions are
           equal. """
        return False

    @abstractmethod
    def isEmpty(self) -> bool:
        """Returns True if the queue is empty. False otherwise."""
        return True

    @abstractmethod
    def clear(self) -> None:
        """Makes the queue become empty. """
        pass

    @abstractmethod
    def peek(self) -> object:
        """Returns the item at the front of the queue.
           Precondition: the queue must not be empty; raises
           a KeyError if the queue is empty. """
        return None

    @abstractmethod
    def enqueue(self, item: object) -> None:
        """Adds an item to the front of the queue. """
        pass

    @abstractmethod
    def dequeue(self) -> object:
        """Removes and returns the item at the front of
           the queue. Precondition: the stack must not be empty;
           raises a KeyError if the queue is empty."""
        return None
