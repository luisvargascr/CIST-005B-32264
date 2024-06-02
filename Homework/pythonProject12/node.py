"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/31/2024

Description: Node
This file is used to represent a Node object.
The Node class will be used to create node objects and
singly linked lists.
"""


class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data: object, nxt: object = None):
        self.data = data
        self.next = nxt
