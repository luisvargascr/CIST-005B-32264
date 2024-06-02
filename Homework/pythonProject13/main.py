"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 04/14/2024

Description: main
This file is used to test the LinkedBST tree.

Test it by:

1) Add numbers 3, 14, 60, -1,2,8, 6, and 7 in the tree data structure.
2) Add 13 to the tree data structure
3) Check if the tree data structure is empty
4) Remove 14 from the tree data structure
5) Add 9 to the tree data structure
6) Remove all items in the tree data structure
7) Check if the tree data structure is empty
"""
from linked_bst import LinkedBST


def call_on_bst_tree():
    """This method instantiates the binary search tree and
       inserts values, iterate through it, checks if its empty
       at various points in the execution, and then removes all items. """
    tree = LinkedBST()
    print("Add numbers 3, 14, 60, -1, 2, 8, 6, and 7 in the tree data structure")
    tree.insert(3)
    tree.insert(14)
    tree.insert(60)
    tree.insert(-1)
    tree.insert(2)
    tree.insert(8)
    tree.insert(6)
    tree.insert(7)
    tree.bfs_iterative()
    print("Add 13 to the tree data structure")
    tree.insert(13)
    tree.bfs_iterative()
    print("Check if the tree data structure is empty. Is the tree empty? %s" % tree.is_empty())
    print("Remove 14 from the tree data structure")
    tree.remove(14)
    tree.bfs_iterative()
    print("Add 9 to the tree data structure")
    tree.insert(9)
    tree.bfs_iterative()
    print("Remove all items in the tree data structure")
    tree.remove_all()
    print("Check if the tree data structure is empty. Is the tree empty? %s" % tree.is_empty())
    tree.bfs_iterative()


if __name__ == '__main__':
    call_on_bst_tree()
