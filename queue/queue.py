import sys

sys.path.insert(0, "../dll")
from doubly_linked_list\
    import DNode, IterDNode, IterDNodeReverse, DoublyLinkedList


class Queue(DoublyLinkedList):
    def enqueue(self, value):
        DoublyLinkedList.insert(self, value)

    def dequeue(self):
        try:
            return DoublyLinkedList.shift(self)
        except ValueError:
            raise ValueError("Queue is empty")

    # consider raising Not Implemented exceptions
    # for other class methods that should not be used
    # with a queue, like append, pop, span_link
