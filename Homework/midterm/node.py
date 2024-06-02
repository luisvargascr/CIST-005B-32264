"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/17/2024

Description: Node
This file is used to represent a Node Object for other
more-advanced data structures to consume.
"""


class Node(object):
    """Node class that represents a node."""

    def __init__(self, item: object = None, nxt: object = None):
        """Constructor"""
        self.value = item
        self.next = nxt
