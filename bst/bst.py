#
# bst.py
#
# Implement a binary tree in Python
#

from ..dll.doubly_linked_list import DNode


class BinarySearchTree(DNode):
    @property
    def left(self):
        return self.link
    @left.setter
    def left(self, value):
        self.link = value

    @property
    def right(self):
        return self.link2
    @right.setter
    def right(self, value):
        self.link2 = value

    def __init__(self, val, left=None, right=None):
        DNode.__init__(self, val, link=left, link2=right)



