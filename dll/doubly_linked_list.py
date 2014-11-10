#
# Implement a doubly linked list
#
# This is supposed to build upon the linked_list implementation
#  however, as near as I can understand PEP366, PEP328 and numerous
#  online questions and explanations regarding relative imports
#  there is virtually no way to do it. The relative path alterations
#  suggested at some web sites (and partly commented out immediately
#  below) fail to work on Travis CI, which probably has a very different
#  of the system path.
#
# Therefore, it is easier to just go to the operating system and do
#       cp ../linked_list/linked_list.py .
#  so that linked_list may be imported from the current directory.
#
# The following two lines are the most recommended online
# import sys
# sys.path.insert(0, "../linked_list")
#
# This one should work, but fails on Travis CI after working locally
from ..linked_list.linked_list import Node, IterNode, LinkedList
#
# Is linked_list.py in the current directory? Use line:
# from linked_list import Node, IterNode, LinkedList


class DNode(Node):
    def __init__(self, val, link=None, link2=None):
        Node.__init__(self, val, link)
        self.link2 = link2


class IterDNode(IterNode):
    pass


class IterDNodeReverse(IterNode):
    def __init__(self, tail):
        self.cur = tail

    def __iter__(self):
        return self

    def next(self):
        if self.cur is not None:
            ret = self.cur
            self.cur = self.cur.link2
            return ret
        else:
            raise StopIteration


class DoublyLinkedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)
        self.tail = None

    def insert(self, val):
        """ insert the value 'val' at the head of the list """

        if val is self:
            # This is a simple check to eliminate the most obvious recursion
            # but to truly detect recursion would require at least an O(n)
            # search on every insert().

            # if recursion is built into the linked list a runtime
            # error will result when __repr__ is called.
            return

        new_dnode = DNode(val, self.head)
        if self.head is not None:
            self.head.link2 = new_dnode
        else:
            self.tail = new_dnode
        self.head = new_dnode
        return

    def append(self, val):
        """ append the value 'val' at the end of the list """

        if val is self:
            # This is a simple check to eliminate the recursion when the
            # val in the append() is the list
            return

        new_dnode = DNode(val, None, self.tail)
        if self.tail is not None:
            self.tail.link = new_dnode
        else:
            self.head = new_dnode
        self.tail = new_dnode
        return

    def pop(self):
        """ pop the first value off the head of the list and return it. """
        if self.head is None:
            # list is empty
            raise ValueError("pop() on empty Stack")

        val = self.head.val
        next_dnode = self.head.link
        if next_dnode is not None:
            next_dnode.link2 = None
        self.head = next_dnode
        return val

    def shift(self, val):
        """ pop the first value off the head of the list and return it. """
        if self.tail is None:
            # list is empty
            raise ValueError("pop() on empty Stack")

        val = self.tail.val
        prev_dnode = self.tail.link2
        if prev_dnode is not None:
            prev_dnode.link = None
        self.tail = prev_dnode
        return val

    def span_link(self, prev, curlink):
        if prev is None:
            self.head = curlink
        else:
            prev.link = curlink

        if curlink is None:
            self.tail = prev
        else:
            curlink.link2 = prev

        return curlink

    def remove(self, val):
        prev = None

        for cur in IterDNode(self.head):
            if cur.val == val:
                return self.span_link(prev, cur.link)
            prev = cur

        # could just return, but spec says it must be in list
        raise ValueError("item to be removed not in list")

