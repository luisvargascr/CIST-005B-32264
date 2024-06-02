"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/23/2024

Description: Palindrome
This file is used to represent a Palindrome object.
The Palindrome class will be used to check if a sentence
is in fact a palindrome or not.

A sample instruction:

1. Create a stack and a queue
2. In a loop, letter by letter push them in the stack and enqueue them in the queue
3. In another loop, compare the letters popping from the stack and dequeuing from
the queue, if they are not the same, break or stop the loop and print that the
entered string is not a palindrome. If all the letters popping from the stack
and dequeuing from the queue are the same, your code should print the entered
string is a palindrome.
"""
from linked_queue import LinkedQueue
from linked_stack import LinkedStack


class Palindrome(object):
    def __init__(self):
        """Constructor. """
        self.__queue = LinkedQueue()
        self.__stack = LinkedStack()

    def is_palindrome(self, sentence: str) -> bool:
        """ Returns True if the sentence is a palindrome. Otherwise, it returns False. """
        sentence = sentence.lower()

        for ch in sentence:
            self.__queue.enqueue(ch)
            self.__stack.push(ch)

        standard_length = len(self.__queue)

        for i in range(0, standard_length + 1):
            char_queue = self.__queue.dequeue()
            char_stack = self.__stack.pop()
            if char_queue != char_stack:
                return False

            return True
