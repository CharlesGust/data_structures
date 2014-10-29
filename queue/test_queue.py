import pytest  # used for the exception testing
import unittest

from queue import Queue


class MyFuncTestCase(unittest.TestCase):
    def test_Queue__init__(self):
        q1 = Queue()
        self.assertEqual(q1.size(), 0)

        with self.assertRaises(ValueError):
            q1.dequeue()

    def test_Queue_enqueue(self):
        q1 = Queue()

        q1.enqueue(0)
        self.assertEqual(q1.size(), 1)
        q1.enqueue(1.2)
        self.assertEqual(q1.size(), 2)
        q1.enqueue("3.4")
        self.assertEqual(q1.size(), 3)
        q1.enqueue([5, 6])
        self.assertEqual(q1.size(), 4)
        q1.enqueue((7, 8))
        self.assertEqual(q1.size(), 5)
        q1.enqueue({9, 10})
        self.assertEqual(q1.size(), 6)

        # simple recursion is silently ignored
        #  but perhaps should raise an error
        q1.enqueue(q1)
        self.assertEqual(q1.size(), 6)

    def test_Queue_dequeue(self):
        q1 = Queue()

        q1.enqueue(0)
        q1.enqueue(1.2)
        q1.enqueue("3.4")
        q1.enqueue([5, 6])
        q1.enqueue((7, 8))
        q1.enqueue({9, 10})

        self.assertEqual(q1.size(), 6)
        self.assertEqual(q1.dequeue(), 0)
        self.assertEqual(q1.size(), 5)
        self.assertEqual(q1.dequeue(), 1.2)
        self.assertEqual(q1.size(), 4)
        self.assertEqual(q1.dequeue(), "3.4")
        self.assertEqual(q1.size(), 3)
        self.assertEqual(q1.dequeue(), [5, 6])
        self.assertEqual(q1.size(), 2)
        self.assertEqual(q1.dequeue(), (7, 8))
        self.assertEqual(q1.size(), 1)
        self.assertEqual(q1.dequeue(), {9, 10})
        self.assertEqual(q1.size(), 0)

        with self.assertRaises(ValueError):
            q1.dequeue()




