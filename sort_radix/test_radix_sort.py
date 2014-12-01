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

    def test_sorts_inorder_tiny(self):
        arr = ['z', 'e', 'b', 'ba', 'bb', 'ee', 'aa', 'ab', 'aaa', 'baa']
        sortarr = sorts(arr)
        for i in range(1, len(sortarr)):
            self.assertGreaterEqual(sortarr[i], sortarr[i-1])

    def test_sorts_randwords(self):
        arr = []
        for i in xrange(0, 100):
            word = ""
            for j in xrange(1, random.randint(1, 15)):
                base = 'A' if random.randint(0, 1) == 0 else 'a'
                word += chr(random.randint(0, 25)+ord(base))
            arr.append(word)
        sortarr = sorts(arr)
        for i in range(1, len(arr)):
            self.assertGreaterEqual(sortarr[i], sortarr[i-1])
