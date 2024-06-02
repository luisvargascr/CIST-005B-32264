"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/23/2024

Description: Node
This file is used to represent a Node object.
The Node class will be used to create node objects and
linked lists.
"""


class Node(object):
    def __init__(self, item: object, nxt: object = None):
        self.value = item
        self.next = nxt
