import py.test
import unittest
from radix_sort import sorti, sorts
import random


class testRadixSort(unittest.TestCase):
    def test__init__(self):
        pass

    def test_sorti_inorder(self):
        arr = [i for i in xrange(0, 10000)]
        sortarr = sorti(arr)
        for i in xrange(1, 10000):
            self.assertGreaterEqual(sortarr[i], sortarr[i-1])

    def test_sorti_revorder(self):
        arr = [i for i in xrange(10000, 0, -1)]
        sortarr = sorti(arr)
        for i in xrange(1, 10000):
            self.assertGreaterEqual(sortarr[i], sortarr[i-1])

    def test_sorti_randorder(self):
        arr = [random.randint(0, 10000) for i in xrange(0, 10000)]
        sortarr = sorti(arr)
        for i in xrange(1, 10000):
            self.assertGreaterEqual(sortarr[i], sortarr[i-1])
