#
# bst.py
#
# Implement a binary tree in Python
#

from ..dll.doubly_linked_list import DNode

class BNode(DNode):
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

    def __init__(self, val=None, left=None, right=None):
        if val is not None:
            DNode.__init__(self, val, link=left, link2=right)


class BinarySearchTree():
    def __init__(self):
        self.head = None
        self.nodeCount = 0

    def _insert(self, val=None, left=None, right=None):
        self.head = BNode(val, left, right)

    def insert(self, val):
        if self.head is None:
            self.head = BNode(val)
        else:
            parent = self.head

            rightChild = False
            leftChild = False
            found = False

            while (not leftChild) and (not rightChild) and (not found):
                if val == parent.val:
                    found = True
                elif val < parent.val:
                    if parent.left is None:
                        leftChild = True
                    else:
                        parent = parent.left
                else:
                    if parent.right is None:
                        rightChild = True
                    else:
                        parent = parent.right
            if found:
                # already have the value, do nothing
                return

            if leftChild:
                parent.left = BNode(val)
            else:
                parent.right = BNode(val)

        self.nodeCount += 1
        return

    def contains(self, val):
        if self.head is None:
            return False

        parent = self.head
        found = False

        while (not found):
            if val == parent.val:
                return True
            elif val < parent.val:
                if parent.left is None:
                    return False
                else:
                    parent = parent.left
            else:
                if parent.right is None:
                    return False
                else:
                    parent = parent.right

    def size(self):
        return self.nodeCount

    def _depth(self, node):
        if node is None:
            return 0
        else:
            return 1 + max([self._depth(node.left), self._depth(node.right)])

    def depth(self):
        return self._depth(self.head)

    def balance(self):
        if self.head is None:
            return 0

        depth_left = self._depth(self.head.left)
        depth_right = self._depth(self.head.right)

        return depth_right - depth_left



