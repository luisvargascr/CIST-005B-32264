"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/23/2024

Description: main
This file is used to test the LinkedStack Implementation.
Test it by:

1) Add numbers from 6 to 16 in the stack.
2) Print the length of the stack
3) Check if the stack is empty
4) Show the item on the top of the stack
5) Remove the last item in the stack
6) Add 45 to the stack
7) Remove all items in the stack
8) Check if the stack is empty
"""
from linked_stack import LinkedStack


def interact_with_stack():
    my_stack = LinkedStack()

    for i in range(6, 16):
        my_stack.push(i)

    print("0) Items in stack %s" % my_stack)
    print("1) The length of the stack is %d." % len(my_stack))
    print("2) Is the stack empty? %s." % my_stack.isEmpty())
    print("3) Item at the top of the stack? %d." % my_stack.peek())
    print("4) Removed the last item in the stack (which is %d)." % my_stack.pop())
    print("5) Add 45 to stack.")
    my_stack.push(45)
    print("6) Items in stack %s" % my_stack)
    print("7) Remove all items in the stack.")
    my_stack.clear()
    print("8) Is the stack empty? %s" % my_stack.isEmpty())
    print("9) Items in stack %s" % my_stack)


if __name__ == '__main__':
    interact_with_stack()
