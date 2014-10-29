import sys

sys.path.insert(0, "../linked_list")
from linked_list import Node, IterNode, LinkedList


class DNode(Node):
    def __init__(self, val, link=None, link2=None):
        Node.__init__(self, val, link)
        self.link2 = link2


class IterDNode(IterNode):
    pass


class IterDNodeReverse(IterNode):
    pass


class DoublyLinkedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
        self.tail = None

    def insert(self, val):
        pass

    def append(self, val):
        pass

    def pop(self, val):
        pass

    def shift(self, val):
        pass

    def remove(self, val):
        pass
