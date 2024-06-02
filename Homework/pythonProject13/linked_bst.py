"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 04/14/2024

Description: LinkedBST
This file is used to represent a LinkedBST object.
"""
import collections
from typing import List

from node_bst import NodeBST


class LinkedBST:
    def __init__(self):
        self.root = None

    #  BFS ALGORITHMS
    def bfs_iterative(self) -> None:
        """This method performs a breadth-first search using an iterative approach."""
        queue = collections.deque([self.root])
        arr = []

        while queue:
            level_count = len(queue)
            for _ in range(level_count):
                node = queue.popleft()
                if node:
                    arr.append(node.value)
                    queue.append(node.left)
                    queue.append(node.right)

        print(arr)

    def bfs_recursive(self) -> None:
        """This method performs a breadth-first search using a recursive approach. """
        if not self.root:
            return
        arr = []

        def print_current_level(node: NodeBST, level: int) -> None:
            """Internal helper method to print the value of the current level in the Binary Search Tree. """
            if not node:
                return
            nonlocal arr
            if level == 1:
                arr.append(node.value)
            elif level > 1:
                print_current_level(node.left, level - 1)
                print_current_level(node.right, level - 1)

        height = self.get_height(self.root)
        for h in range(1, height + 1):
            print_current_level(self.root, h)
        print(arr)

    # DFS ALGORITHMS
    def dfs_iterative(self) -> None:
        """This method performs a depth first search using an iterative approach. """
        # DFS Iterative will traverse inorder
        stack = []
        node = self.root
        values = []

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            values.append(node.value)
            node = node.right
        print("(Traverses INORDER)")
        print(values)

    def dfs_recursive(self) -> None:
        """This method performs a depth first search using a recursive approach. """
        # DFS Iterative will traverse preorder
        values = []

        def dfs(node: NodeBST) -> None:
            if not node:
                return
            nonlocal values
            values.append(node.value)
            dfs(node.left)
            dfs(node.right)

        dfs(self.root)
        print("(Traverses PREORDER)")
        print(values)

    def __preorder(self, node: NodeBST, arr: List[object]) -> None:
        """This method performs preorder traversal on the Binary Search Tree. """
        if node:
            arr.append(node.value)
            self.__preorder(node.left, arr)
            self.__preorder(node.right, arr)

    def __inorder(self, node: NodeBST, arr: List[object]) -> None:
        """This method performs inorder traversal on the Binary Search Tree. """
        if node:
            self.__inorder(node.left, arr)
            arr.append(node.value)
            self.__inorder(node.right, arr)

    def __postorder(self, node: NodeBST, arr: List[object]) -> None:
        """This method performs postorder traversal on the Binary Search Tree. """
        if node:
            self.__postorder(node.left, arr)
            self.__postorder(node.right, arr)
            arr.append(node.value)

    def preorder(self):
        """This method calls on the preorder traversal method and appends results to an array. """
        arr = []
        self.__preorder(self.root, arr)
        print(arr)

    def inorder(self):
        """This method calls on the inorder traversal method and appends results to an array. """
        arr = []
        self.__inorder(self.root, arr)
        print(arr)

    def postorder(self):
        """This method calls on the postorder traversal method and appends results to an array. """
        arr = []
        self.__postorder(self.root, arr)
        print(arr)

    def diameter_of_binary_tree(self) -> int:
        """This method figures out the diameter of a binary search tree and returns its diameter value. """
        res = 0

        def dfs(node: NodeBST) -> int:
            nonlocal res
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right)
            return 1 + max(left, right)

        dfs(self.root)
        return res

    def get_height(self, node: NodeBST) -> int:
        """This method figures out the height of a binary search tree and returns its height value. """
        if not node and self:
            return 0
        return node.height

    def __get_balance_factor(self, node: NodeBST) -> int:
        """This method calculates the balance factor of a binary search tree and returns this value. """
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def insert(self, exp_value: int) -> None:
        """This method inserts a new value into a binary search tree. """
        self.root = self.__insert(self.root, exp_value)

    def __insert(self, node: NodeBST, value: object) -> NodeBST:
        """This method inserts a new value into a binary search tree and helps to maintain
           its characteristics of being a balanced binary search tree. """
        if not node:
            return NodeBST(value)
        elif value < node.value:
            node.left = self.__insert(node.left, value)
        else:
            node.right = self.__insert(node.right, value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance_factor = self.__get_balance_factor(node)

        if balance_factor > 1 and value < node.left.value:
            return self.__right_rotate(node)
        if balance_factor < -1 and value > node.right.value:
            return self.__left_rotate(node)
        if balance_factor > 1 and value > node.left.value:
            node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)
        if balance_factor < -1 and value < node.right.value:
            node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)

        return node

    def __right_rotate(self, node: NodeBST):
        """This method performs right rotation on a subtree if required to keep balance. """
        left_node = node.left
        right_of_left = left_node.right

        left_node.right = node
        node.left = right_of_left

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left_node.height = 1 + max(self.get_height(left_node.left), self.get_height(left_node.right))

        return left_node

    def __left_rotate(self, node: NodeBST):
        """This method performs left rotation on a subtree if required to keep balance. """
        right_node = node.right
        left_of_right = right_node.left

        right_node.left = node
        node.right = left_of_right

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right_node.height = 1 + max(self.get_height(right_node.left), self.get_height(right_node.right))

        return right_node

    def __get_min_value_node(self, node: NodeBST) -> NodeBST | None:
        """This method gets the child node with the minimum value for a given node. """
        if node is None or node.left is None:
            return node

        return self.__get_min_value_node(node.left)

    def __delete(self, node: NodeBST, key: object) -> NodeBST:
        """This method deletes a node based on its key value. """
        # Step 1 - Perform standard BST delete
        if not node:
            return node

        elif key < node.value:
            node.left = self.__delete(node.left, key)

        elif key > node.value:
            node.right = self.__delete(node.right, key)

        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.__get_min_value_node(node.right)
            node.value = temp.value
            node.right = self.__delete(node.right,
                                       temp.value)

        # If the tree has only one node,
        # simply return it
        if node is None:
            return node

        # Step 2 - Update the height of the
        # ancestor node
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        # Step 3 - Get the balance factor
        balance = self.__get_balance_factor(node)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.__get_balance_factor(node.left) >= 0:
            return self.__right_rotate(node)

        # Case 2 - Right Right
        if balance < -1 and self.__get_balance_factor(node.right) <= 0:
            return self.__left_rotate(node)

        # Case 3 - Left Right
        if balance > 1 and self.__get_balance_factor(node.left) < 0:
            node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)

        # Case 4 - Right Left
        if balance < -1 and self.__get_balance_factor(node.right) > 0:
            node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)

        return node

    def remove(self, value: object) -> bool:
        """This method removes a value from the binary search tree and
           return True if it was successful in doing so or False if otherwise. """
        root = self.root
        deleted_node = self.__delete(root, value)
        return False if deleted_node is None else True

    def remove_all(self):
        """This method removes all nodes from the binary search tree. """
        self.root = self.__remove_all(self.root)

    def __remove_all(self, node: NodeBST) -> NodeBST:
        """This method recursively removes all nodes from the binary search tree. """
        if node:
            self.__remove_all(node.left)
            self.__remove_all(node.right)
            node.value = None
            node.left = None
            node.right = None
            node = None

        return node

    def is_empty(self) -> bool:
        """This method checks if the binary search tree is empty. If it is,
           it returns True. Otherwise, it returns False. """
        return True if self.root is None else False
