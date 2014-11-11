#!/usr/bin/env python

"""
code that tests the LinkedList class defined in linked_list.py

can be run with py.test
"""

import pytest  # used for the exception testing
import unittest

from bst import BinarySearchTree

class BSTTestCases(unittest.TestCase):
    def test_primitives(self):
        # construct a tree using BinarySearchTree primitives
        # This tree has only left links
        l5 = BinarySearchTree(0, left=None, right=None)
        l4 = BinarySearchTree(1, left=l5, right=None)
        l3 = BinarySearchTree(2, left=l4, right=None)
        l2 = BinarySearchTree(3, left=l3, right=None)
        l1 = BinarySearchTree(4, left=l2, right=None)
        head = BinarySearchTree(5, left=l1, right=None)

if __name__ == "__main__":
    unittest.main()
