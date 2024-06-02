"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/31/2024

Description: AbstractList
This file is used to represent an Abstract List Class.
Concrete classes that use this class must implement the methods listed below.
"""

from abc import abstractmethod


class AbstractList():
    """AbstractList class that represents a List Abstract Data Type (ADT). """

    @abstractmethod
    def Insert(self, index: int, item: object) -> None:
        """Inserts an item inside the list. """
        pass

    @abstractmethod
    def Pop(self, index: int = 0) -> object:
        """Pops an item from the list at the provided index. If no index is provided,
           it pops the last item from the list. """
        return None

    # Content-Based Operations
    @abstractmethod
    def add(self, item: object) -> object:
        """Adds an item to the list. """
        return None

    @abstractmethod
    def remove(self, item: object) -> None:
        """Removes an item from the list.
           Precondition: item is in self.
           Raises: ValueError if item is not in self.
           Post condition: item is removed from self. """
        pass

    @abstractmethod
    def clear(self) -> None:
        """Removes all items from the list. """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Returns True if the list is empty. Else, False. """
        return True
