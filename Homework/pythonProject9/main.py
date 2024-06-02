"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 02/17/2024

Description: This program solves Chapter 4 Exercise 2:
Write a Node class for singly linked structure.
Define 3 node objects with which to put these data
in them. "4", "-7", "34"

"""


class Node(object):
    """
    This class represents a node that can be used for other classes to use
    """

    def __init__(self, data: object = None, nxt: object = None):
        self.data = data
        self.node = nxt


class SinglyLinkedList(object):
    """
    This class represents a simple singly linked list
    """

    def __init__(self):
        """
        Constructor
        """
        self.head = None

    def insert(self, data: object) -> None:
        """
        Method Name: insert
        Description: This method inserts records at the end of the linked list.
        :param data: data, the actual object that you want to add to the linked list.
        :return: it is a void method and thus returns no value (None).
        """
        if not self.head:
            self.head = Node(data)
        else:
            tmp = self.head
            while tmp.node:
                tmp = tmp.node

            tmp.node = Node(data, tmp.node)

    def print(self) -> None:
        """
        Method Name: print
        Description: This method prints the contents of a linked list
        :param: No parameters
        :return: it is a void method and thus returns no value (None).
        """
        curr = self.head
        if not curr:
            print("Linked List is empty!")
            return

        value_list = []
        while curr:
            value_list.append(str(curr.data))
            curr = curr.node

        print("The content of the linked list is '%s'." % ("->".join(value_list)))
        value_list.clear()


def use_linked_list() -> None:
    """
    Method Name: use_linked_list
    Description: This method creates an instance of SinglyLinkedList
    and inserts three values, "4", "-7", and "34" and then prints them out.
    :param: No parameters
    :return: it is a void method and thus returns no value (None).
    """
    linked_list = SinglyLinkedList()
    linked_list.insert("4")
    linked_list.insert("-7")
    linked_list.insert("34")
    linked_list.print()

    """
    Define 3 node objects with which to put these data
    in them. "4", "-7", "34"
    
    Description: Below, node1 will have a link to node2, 
    and node2 to node3. Thus, the linked list is built in 
    the reversed order and the content will be kept 
    as "4" -> "-7" -> "34" inside node1 (as it is expected).
    """

    node3 = Node("34", None)
    node2 = Node("-7", node3)
    node1 = Node("4", node2)


if __name__ == '__main__':
    use_linked_list()
