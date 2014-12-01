#!/usr/bin/env python

"""
code that tests the LinkedList class defined in linked_list.py

can be run with py.test
"""

import pytest  # used for the exception testing
import unittest

from bst import BNode, BinarySearchTree

class BNodeTestCases(unittest.TestCase):
    def test_primitives(self):
        # construct a tree using BinarySearchTree primitives
        # This tree has only left links
        l5 = BNode(0, left=None, right=None)
        l4 = BNode(1, left=l5, right=None)
        l3 = BNode(2, left=l4, right=None)
        l2 = BNode(3, left=l3, right=None)
        l1 = BNode(4, left=l2, right=None)
        head = BNode(5, left=l1, right=None)

    def test_properties(self):
        # test get for left, right properties
        n0 = BNode(0, None, None)
        n2 = BNode(2, None, None)
        n1 = BNode(1, n0, n2)

        self.assertEqual(n0.val, 0)
        self.assertEqual(n2.val, 2)
        self.assertEqual(n1.val, 1)
        self.assertEqual(n1.left, n0)
        self.assertEqual(n1.right, n2)
        self.assertEqual(n1.left.val, 0)
        self.assertEqual(n1.right.val, 2)

        # test set for left, right properties
        n3 = BNode(3, None, None)
        n2.right = n3
        nn1 = BNode(-1, None, None)
        n0.left = nn1

class BinarySearchTreeTestCases(unittest.TestCase):
    def test___init__(self):
        bst1 = BinarySearchTree()

        self.assertIsNone(bst1.head)
        self.assertEqual(bst1.contains(0), False)
        self.assertEqual(bst1.contains(None), False)
        self.assertEqual(bst1.size(), 0)
        self.assertEqual(bst1.depth(), 0)
        self.assertEqual(bst1.balance(), 0)

    def test_insert_nobalance(self):

        bst1 = BinarySearchTree()
        bst2 = BinarySearchTree()
        bst3 = BinarySearchTree()
        bst4 = BinarySearchTree()
        bst5 = BinarySearchTree()
        bst6 = BinarySearchTree()

        # multiple passes through to ensure duplicates not added
        for i in xrange(3):

            bst1.insert(0)
            bst1.insert(1)
            bst1.insert(2)

            # assumes no balancing
            self.assertEqual(bst1.head.val, 0)
            self.assertIsNone(bst1.head.left)
            self.assertIsNotNone(bst1.head.right)
            self.assertEqual(bst1.head.right.val, 1)
            self.assertIsNone(bst1.head.right.left)
            self.assertIsNotNone(bst1.head.right.right)
            self.assertEqual(bst1.head.right.right.val, 2)
            self.assertIsNone(bst1.head.right.right.left)
            self.assertIsNone(bst1.head.right.right.right)


            bst2.insert(1)
            bst2.insert(2)
            bst2.insert(0)

            # assumes no balancing
            self.assertEqual(bst2.head.val, 1)
            self.assertIsNotNone(bst2.head.left)
            self.assertIsNotNone(bst2.head.right)
            self.assertEqual(bst2.head.right.val, 2)
            self.assertEqual(bst2.head.left.val, 0)
            self.assertIsNone(bst2.head.left.left)
            self.assertIsNone(bst2.head.left.right)
            self.assertIsNone(bst2.head.right.left)
            self.assertIsNone(bst2.head.right.right)

            bst3.insert(2)
            bst3.insert(0)
            bst3.insert(1)

            # assumes no balancing
            self.assertEqual(bst3.head.val, 2)
            self.assertIsNotNone(bst3.head.left)
            self.assertIsNone(bst3.head.right)
            self.assertEqual(bst3.head.left.val, 0)
            self.assertIsNone(bst3.head.left.left)
            self.assertIsNotNone(bst3.head.left.right)
            self.assertEqual(bst3.head.left.right.val, 1)
            self.assertIsNone(bst3.head.left.right.left)
            self.assertIsNone(bst3.head.left.right.right)

            bst4.insert(2)
            bst4.insert(1)
            bst4.insert(0)

            # assumes no balancing
            self.assertEqual(bst4.head.val, 2)
            self.assertIsNotNone(bst4.head.left)
            self.assertIsNone(bst4.head.right)
            self.assertEqual(bst4.head.left.val, 1)
            self.assertIsNone(bst4.head.left.right)
            self.assertIsNotNone(bst4.head.left.left)
            self.assertEqual(bst4.head.left.left.val, 0)
            self.assertIsNone(bst4.head.left.left.left)
            self.assertIsNone(bst4.head.left.left.right)

            bst5.insert(0)
            bst5.insert(2)
            bst5.insert(1)

            # assumes no balancing
            self.assertEqual(bst5.head.val, 0)
            self.assertIsNone(bst5.head.left)
            self.assertIsNotNone(bst5.head.right)
            self.assertEqual(bst5.head.right.val, 2)
            self.assertIsNotNone(bst5.head.right.left)
            self.assertIsNone(bst5.head.right.right)
            self.assertEqual(bst5.head.right.left.val, 1)
            self.assertIsNone(bst5.head.right.left.left)
            self.assertIsNone(bst5.head.right.left.right)

            bst6.insert(1)
            bst6.insert(0)
            bst6.insert(2)

            # assumes no balancing
            self.assertEqual(bst6.head.val, 1)
            self.assertIsNotNone(bst6.head.left)
            self.assertIsNotNone(bst6.head.right)
            self.assertEqual(bst6.head.left.val, 0)
            self.assertEqual(bst6.head.right.val, 2)
            self.assertIsNone(bst6.head.left.left)
            self.assertIsNone(bst6.head.left.right)
            self.assertIsNone(bst6.head.right.left)
            self.assertIsNone(bst6.head.right.right)

    def test_contains_simple(self):
        bst1 = BinarySearchTree()
        bst2 = BinarySearchTree()
        bst3 = BinarySearchTree()
        bst4 = BinarySearchTree()
        bst5 = BinarySearchTree()
        bst6 = BinarySearchTree()

        bst1.insert(0)
        bst1.insert(1)
        bst1.insert(2)

        self.assertTrue(bst1.contains(0))
        self.assertTrue(bst1.contains(1))
        self.assertTrue(bst1.contains(2))

        bst2.insert(1)
        bst2.insert(2)
        bst2.insert(0)

        self.assertTrue(bst2.contains(0))
        self.assertTrue(bst2.contains(1))
        self.assertTrue(bst2.contains(2))

        bst3.insert(2)
        bst3.insert(0)
        bst3.insert(1)

        self.assertTrue(bst3.contains(0))
        self.assertTrue(bst3.contains(1))
        self.assertTrue(bst3.contains(2))

        bst4.insert(2)
        bst4.insert(1)
        bst4.insert(0)

        self.assertTrue(bst4.contains(0))
        self.assertTrue(bst4.contains(1))
        self.assertTrue(bst4.contains(2))

        bst5.insert(0)
        bst5.insert(2)
        bst5.insert(1)

        self.assertTrue(bst5.contains(0))
        self.assertTrue(bst5.contains(1))
        self.assertTrue(bst5.contains(2))

        bst6.insert(1)
        bst6.insert(0)
        bst6.insert(2)

        self.assertTrue(bst6.contains(0))
        self.assertTrue(bst6.contains(1))
        self.assertTrue(bst6.contains(2))

    def test_size(self):
        for size in [1, 2, 3, 4, 7, 8, 15, 26, 100, 417, 5694]:
            bst = BinarySearchTree()

            for i in xrange(size):
                bst.insert(i)

            self.assertEqual(bst.size(), size)

    def test_depth_nobalance(self):
        bst1 = BinarySearchTree()
        bst2 = BinarySearchTree()
        bst3 = BinarySearchTree()
        bst4 = BinarySearchTree()
        bst5 = BinarySearchTree()
        bst6 = BinarySearchTree()

        bst1.insert(0)
        bst1.insert(1)
        bst1.insert(2)

        self.assertEqual(bst1.depth(),3)

        bst2.insert(1)
        bst2.insert(2)
        bst2.insert(0)

        self.assertEqual(bst2.depth(),2)

        bst3.insert(2)
        bst3.insert(0)
        bst3.insert(1)

        self.assertEqual(bst3.depth(),3)

        bst4.insert(2)
        bst4.insert(1)
        bst4.insert(0)

        self.assertEqual(bst4.depth(),3)

        bst5.insert(0)
        bst5.insert(2)
        bst5.insert(1)

        self.assertEqual(bst5.depth(),3)

        bst6.insert(1)
        bst6.insert(0)
        bst6.insert(2)

        self.assertEqual(bst6.depth(),2)

    def test_balance_nobalance(self):
        bst1 = BinarySearchTree()
        bst2 = BinarySearchTree()
        bst3 = BinarySearchTree()
        bst4 = BinarySearchTree()
        bst5 = BinarySearchTree()
        bst6 = BinarySearchTree()

        bst1.insert(0)
        bst1.insert(1)
        bst1.insert(2)

        self.assertEqual(bst1.balance(),2)

        bst2.insert(1)
        bst2.insert(2)
        bst2.insert(0)

        self.assertEqual(bst2.balance(),0)

        bst3.insert(2)
        bst3.insert(0)
        bst3.insert(1)

        self.assertEqual(bst3.balance(),-2)

        bst4.insert(2)
        bst4.insert(1)
        bst4.insert(0)

        self.assertEqual(bst4.balance(),-2)

        bst5.insert(0)
        bst5.insert(2)
        bst5.insert(1)

        self.assertEqual(bst5.balance(),2)

        bst6.insert(1)
        bst6.insert(0)
        bst6.insert(2)

        self.assertEqual(bst6.balance(),0)

    def test_delete_simple(self):
        bst1 = BinarySearchTree()
        bst2 = BinarySearchTree()
        bst3 = BinarySearchTree()
        bst4 = BinarySearchTree()
        bst5 = BinarySearchTree()
        bst6 = BinarySearchTree()

        bst1.insert(0)
        bst1.insert(1)
        bst1.insert(2)

        bst1.delete(1)
        self.assertEqual(bst1.size(),2)
        bst1.delete(0)
        self.assertEqual(bst1.size(),1)
        bst1.delete(2)
        self.assertEqual(bst1.size(),0)

        bst2.insert(1)
        bst2.insert(2)
        bst2.insert(0)

        bst2.delete(0)
        self.assertEqual(bst2.size(),2)
        bst2.delete(2)
        self.assertEqual(bst2.size(),1)
        bst2.delete(1)
        self.assertEqual(bst2.size(),0)

        bst3.insert(2)
        bst3.insert(0)
        bst3.insert(1)

        bst3.delete(2)
        self.assertEqual(bst3.size(),2)
        bst3.delete(1)
        self.assertEqual(bst3.size(),1)
        bst3.delete(0)
        self.assertEqual(bst3.size(),0)

        bst4.insert(2)
        bst4.insert(1)
        bst4.insert(0)

        bst4.delete(2)
        self.assertEqual(bst4.size(),2)
        bst4.delete(0)
        self.assertEqual(bst4.size(),1)
        bst4.delete(1)
        self.assertEqual(bst4.size(),0)

        bst5.insert(0)
        bst5.insert(2)
        bst5.insert(1)

        bst5.delete(1)
        self.assertEqual(bst5.size(),2)
        bst5.delete(2)
        self.assertEqual(bst5.size(),1)
        bst5.delete(0)
        self.assertEqual(bst5.size(),0)

        bst6.insert(1)
        bst6.insert(0)
        bst6.insert(2)

        bst6.delete(0)
        self.assertEqual(bst6.size(),2)
        bst6.delete(1)
        self.assertEqual(bst6.size(),1)
        bst6.delete(2)
        self.assertEqual(bst6.size(),0)

    def test_delete_complex(self):
        for size in [1, 2, 3, 4, 7, 8, 15, 26, 100, 417, 5694]:
            bst = BinarySearchTree()

            for i in xrange(size):
                bst.insert(i)

            self.assertEqual(bst.size(), size)

            for i in xrange(size):
                bst.delete(i)

            self.assertEqual(bst.size(), 0)

    def test_WorstCase_insert(self):
        bst1 = BinarySearchTree()
        bst2 = BinarySearchTree()

        for i in xrange(100):
            bst1.insert(i)
            bst2.insert(100-i)

        self.assertEqual(bst1.depth(), 100)
        self.assertEqual(bst2.depth(), 100)

    def test_perfect_insert(self):
        def insert_mids(tree, start, end):
            mid = start + int((end-start)//2)
            if (mid == start) or (mid == end):
                return
            else:
                tree.insert(mid)
                insert_mids(tree, start, mid)
                insert_mids(tree, mid, end)

        bst2 = BinarySearchTree()
        insert_mids(bst2, 0, 4)
        self.assertEqual(bst2.depth(), 2)

        bst4 = BinarySearchTree()
        insert_mids(bst4, 0, 16)
        self.assertEqual(bst4.depth(), 4)

        bst6 = BinarySearchTree()
        insert_mids(bst6, 0, 64)
        self.assertEqual(bst6.depth(), 6)

        bst8 = BinarySearchTree()
        insert_mids(bst8, 0, 256)
        self.assertEqual(bst8.depth(), 8)

        bst10 = BinarySearchTree()
        insert_mids(bst10, 0, 1024)
        self.assertEqual(bst10.depth(), 10)

        for i in xrange(4):
            bst2.delete(i)

        for i in xrange(64):
            bst6.delete(i)

        for i in xrange(256):
            bst8.delete(i)

        for i in xrange(1024):
            bst10.delete(i)

        self.assertEqual(bst2.size(), 0)
        self.assertEqual(bst2.depth(), 0)

        self.assertEqual(bst6.size(), 0)
        self.assertEqual(bst6.depth(), 0)

        self.assertEqual(bst8.size(), 0)
        self.assertEqual(bst8.depth(), 0)

        self.assertEqual(bst10.size(), 0)
        self.assertEqual(bst10.depth(), 0)

    # def test_inorder(self):
    #     bst1 = BinarySearchTree()
    #     bst2 = BinarySearchTree()
    #     bst3 = BinarySearchTree()
    #     bst4 = BinarySearchTree()
    #     bst5 = BinarySearchTree()
    #     bst6 = BinarySearchTree()

    #     bst1.insert(0)
    #     bst1.insert(1)
    #     bst1.insert(2)

    #     for x in bst1.in_order():
    #         self.assertGreaterEqual(x, 0)
    #         self.assertLessEqual(x, 2)

        # bst2.insert(1)
        # bst2.insert(2)
        # bst2.insert(0)

        # self.assertTrue(bst2.contains(0))
        # self.assertTrue(bst2.contains(1))
        # self.assertTrue(bst2.contains(2))

        # bst3.insert(2)
        # bst3.insert(0)
        # bst3.insert(1)

        # self.assertTrue(bst3.contains(0))
        # self.assertTrue(bst3.contains(1))
        # self.assertTrue(bst3.contains(2))

        # bst4.insert(2)
        # bst4.insert(1)
        # bst4.insert(0)

        # self.assertTrue(bst4.contains(0))
        # self.assertTrue(bst4.contains(1))
        # self.assertTrue(bst4.contains(2))

        # bst5.insert(0)
        # bst5.insert(2)
        # bst5.insert(1)

        # self.assertTrue(bst5.contains(0))
        # self.assertTrue(bst5.contains(1))
        # self.assertTrue(bst5.contains(2))

        # bst6.insert(1)
        # bst6.insert(0)
        # bst6.insert(2)

        # self.assertTrue(bst6.contains(0))
        # self.assertTrue(bst6.contains(1))
        # self.assertTrue(bst6.contains(2))
        # pass

    def test_pre_order(self):
        pass

    def test_post_order(self):
        pass

    def test_breadth_first(self):
        pass


if __name__ == "__main__":
    unittest.main()
