#!/usr/bin/python
#
# bst.py
#
# Implement a binary tree in Python
#

# CMGTODO: Until the package/module system in Python supports it,
# the data_structures needed are being COPIED into this file from
# linked_list.py
# doubly_linked_list.py
#from ..dll.doubly_linked_list import DNode

# BEGIN linked_list.py
class Node():
    def __init__(self, val, link=None):
        self.val = val
        self.link = link



# END linked_list.py

# BEGIN doubly_linked_list.py
class DNode(Node):
    def __init__(self, val, link=None, link2=None):
        Node.__init__(self, val, link)
        self.link2 = link2

# END doubly_linked_list.py

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

    def _merge(self, parent, left, right):
        if left is None:
            return right
        if right is None:
            return left

        lplace = left
        rplace = right
        while True:
            if lplace.right is None:
                lplace.right = right
                return left
            if rplace.left is None:
                rplace.left = left
                return right
            lplace = lplace.right
            rplace = rplace.left

    def delete(self, val):
        """
        remove val from the tree if present, if not present this method
        is a no-op. Return None in all cases
        """
        # print "Enter delete()"
        if self.head is None:
            return None

        # print "set Booleans"
        parent = None
        current = self.head
        found = False

        # print "enter while"
        while (not found):
            if val == current.val:
                found = True
            elif val < current.val:
                if current.left is None:
                    return None
                else:
                    parent = current
                    current = current.left
            else:
                if current.right is None:
                    return None
                else:
                    parent = current
                    current = current.right

        # print "decrement nodeCount"
        self.nodeCount -= 1

        # print "nodeCount"
        if self.nodeCount == 0:
            self.head = None
            return None

        # print "check parent"
        if parent is None:
            # means self.head - the top node - matched the value
            self.head = self._merge(None, self.head.left, self.head.right)
            return None

        # print "check depth"
        depth_left = self._depth(current.left)
        depth_right = self._depth(current.right)

        if depth_left < depth_right:
            # right is deeper, rotate right node up
            if parent.right == current:
                parent.right = current.right
                if ((current.left is not None) and
                    (parent.right.left is not None)):
                    # collision! parent.right.left and current.left
                    parent.right.left = self._merge(parent.right,
                                                    current.left,
                                                    parent.right.left)
            else:
                # parent left == current
                parent.left = current.right
                if ((current.left is not None) and
                    (parent.left.left is not None)):
                    # collision! parent.left.left and current.left
                    parent.left.left = self._merge(parent.left,
                                                   current.left,
                                                   parent.left.left)
        else:
            # left is deeper, or they are equal
            if parent.right == current:
                parent.right = current.left
                if ((current.right is not None) and
                    (parent.right.right is not None)):
                    # collision! parent.right.right and current.right
                    parent.right.right = self._merge(parent.right,
                                                     parent.right.right,
                                                     current.right)
            else:
                # parent.left == current
                parent.left = current.left
                if ((current.right is not None) and
                    (parent.left.right is not None)):
                    # collision! parent.left.right and current.right
                    parent.left.right = self._merge(parent.left,
                                                    parent.left.right,
                                                    current.right)
        return None



