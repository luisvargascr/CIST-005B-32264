"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 02/25/2024

Description: BagInterface
"""


class BagInterface(object):
    def __init__(self, source_collection: object = None):
        pass

    def isEmpty(self):
        return True

    def __len__(self):
        return 0

    def __str__(self):
        return ""

    def __iter__(self):
        return None

    def __add__(self, other):
        return None

    def __eq__(self, other):
        return False

    def count(self, item):
        return 0

    def clear(self):
        pass

    def add(self, item):
        pass

    def remove(self, item):
        pass
