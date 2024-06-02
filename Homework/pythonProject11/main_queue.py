"""
West Valley College
CIST-005B-32264
Student Name: Luis Vargas Chacon
Student ID: G08280596
Email: lvargasc@mywvm.wvm.edu
Team Name: The Infinite Loop
Date: 03/23/2024

Description: main_queue
This file is used to test the LinkedQueue Implementation.
Test it by:

1) Add numbers from 25 to 35 in the queue.
2) Print the length of the queue
3) Check if the queue is empty
4) Show the item at the front of the queue
5) Remove the first item in the queue
6) Add 95 to the queue
7) Remove all items in the queue
8) Check if the queue is empty
"""
from linked_queue import LinkedQueue


def interact_with_queue():
    my_queue = LinkedQueue()

    for i in range(25, 35):
        my_queue.enqueue(i)

    print("0) Items in queue %s" % my_queue)
    print("1) The length of the queue is %d." % len(my_queue))
    print("2) Is the queue empty? %s." % my_queue.isEmpty())
    print("3) Item at the front of the queue? %d." % my_queue.peek())
    print("4) Removed the first item in the queue (which is %d)." % my_queue.dequeue())
    print("5) Add 95 to queue.")
    my_queue.enqueue(95)
    print("6) Items in queue %s" % my_queue)
    print("7) Remove all items in the queue.")
    my_queue.clear()
    print("8) Is the queue empty? %s" % my_queue.isEmpty())
    print("9) Items in queue %s" % my_queue)


if __name__ == '__main__':
    interact_with_queue()
