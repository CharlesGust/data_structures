#!/usr/bin/env python

"""
code that tests the Stack class defined in stack.py

Because this class is mostly implemented as derived from LinkedList
 it only tests the added Stack functionality and interface
"""

import unittest

from stack import Stack


class MyFuncTestCase(unittest.TestCase):
    def test_Stack_push(self):
        l1 = Stack()
        l1.push(0)
        l1.push(2)
        l1.push(1)

        Val1 = l1.pop()
        self.assertEqual(Val1, 1)

        Val2 = l1.pop()
        self.assertEqual(Val2, 2)

        Val0 = l1.pop()
        self.assertEqual(Val0, 0)

    def test_Stack_remove(self):
        l1 = Stack()
        l1.push(2)
        with self.assertRaises(NotImplementedError):
            l1.remove(None)

    def test_Stack_remove_val(self):
        l1 = Stack()
        l1.push(2)
        with self.assertRaises(NotImplementedError):
            l1.remove_val(2)

    def test_Stack_search(self):
        l1 = Stack()
        l1.push(2)
        with self.assertRaises(NotImplementedError):
            l1.remove_val(2)

    def test_Stack_insert(self):
        l1 = Stack()
        with self.assertRaises(NotImplementedError):
            l1.insert(2)

if __name__ == "__main__":
    unittest.main()
