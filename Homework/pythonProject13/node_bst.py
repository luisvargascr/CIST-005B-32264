"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 04/14/2024

Description: NodeBST
This file is used to represent a NodeBST object
which is to be used to build a Binary Search Tree (BST).
"""


class NodeBST:
    def __init__(self, value: object = None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
