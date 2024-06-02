"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/31/2024

Description: main
This file is used to test the LinkedList Implementation.
Test it by:

1) Add numbers from 14 to 19 in the list data structure.
2) Print the length of the list data structure
3) Check if the list data structure is empty
4) Show all the items in the list data structure
5) Remove 15 from the list data structure
6) Add 95 to the list data structure
7) Remove all items in the list data structure
8) Check if the list data structure is empty
"""
from linked_list import LinkedList


def interact_with_list():
    my_list = LinkedList()

    for i in range(14, 19):
        my_list.add(i)

    print("1) The length of the list data structure is %d." % len(my_list))
    print("2) Is the list data structure empty? %s." % my_list.is_empty())
    print("3) Show all items in the list %s" % my_list)
    print("4) Remove 15 from the list data structure.")
    my_list.remove(15)
    print("5) The length of the list data structure is %d." % len(my_list))
    print("6) Show all items in the list %s" % my_list)
    print("7) Add 95 to the list data structure.")
    my_list.add(95)
    print("8) The length of the list data structure is %d." % len(my_list))
    print("9) Items in the list %s" % my_list)
    print("10) Remove all items in the list.")
    my_list.clear()
    print("11) Is the list empty? %s" % my_list.is_empty())
    print("12) Items in list %s" % my_list)
    print("13) The length of the list data structure is %d." % len(my_list))


if __name__ == '__main__':
    interact_with_list()

