import py.test
import unittest
from insertion_sort import sort
import random

class testInsertionSort(unittest.TestCase):
    def test__init__(self):
        pass

    def test_sort_inorder(self):
        arr = [i for i in xrange(0, 10000)]
        sortarr = sort(arr)
        for i in xrange(1, 10000):
            self.assertGreaterEqual(sortarr[i], sortarr[i-1])

    def test_sort_revorder(self):
        arr = [i for i in xrange(10000, 0, -1)]
        sortarr = sort(arr)
        for i in xrange(1, 10000):
            self.assertGreaterEqual(sortarr[i], sortarr[i-1])

    def test_sortrandorder(self):
        arr = [random.randint(0, 10000) for i in xrange(0,10000)]
        sortarr = sort(arr)
        for i in xrange(1, 10000):
            self.assertGreaterEqual(sortarr[i], sortarr[i-1])
