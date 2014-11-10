#!/usr/bin/env python

"""
code that tests the HashTable class defined in hashtable.py

can be run with py.test
"""

import pytest  # used for the exception testing
import unittest

from hashtable import HashTable


class MyFuncTestCase(unittest.TestCase):
    hash_size_instances = [1, 2, 4, 6, 7, 8, 16, 40, 127, 217, 1000, 5000]
    key_instances =\
        ["", "a", "ab", "ba", "aa", "bb", "z", "zyxw",
         "John", "Paul", "George", "Ringo", "john", "paul",
         "$", "$$", "$$$", "$$$$", "$$$$$",
         "\\/?,.][}{)(*&^%$#@!;'+=-_~",
         "apojwejksdkjlagNlknnlnanlasdfKLLKHKLHSkJANWEROP",
         "When", "in", "the", "course", "of", "human", "events", "it",
         "becomes", "necessary", "for", "one", "people", "to", "dissolve",
         "the", "political", "bands", "which", "have", "connected", "them",
         "with", "another", "and", "to", "assume", "among", "the", "powers",
         "of", "the", "earth", "the", "separate", "and", "equal", "station",
         "to", "which", "the", "Laws", "of", "Nature", "and", "of", "Nature's",
         "God", "entitle", "them", "a", "decent", "respect", "to", "the",
         "opinions", "of", "mankind", "requires", "that", "they", "should",
         "declare", "the", "causes", "which", "impel", "them", "to", "the",
         "separation."
         ]
    non_string_instances = [0, 1.2, (0, 1), [0, 1], {0, 1},
                            HashTable.hash
                            ]

    def test_HashTable___init__(self):
        with self.assertRaises(IndexError):
            hneg1 = HashTable(-1)
            h0 = HashTable(0)

        # a HashTable of 1 can be created, but will have a single
        # bucket and all hashes will go to slot 0
        h1 = HashTable(1)

        for hs in MyFuncTestCase.hash_size_instances:
            h1 = HashTable(hs)

    def test_hash(self):
        upper = 16
        h1 = HashTable(upper)

        with self.assertRaises(TypeError):
            for inst in MyFuncTestCase.non_string_instances:
                v = h1.hash(inst)

        for hs in MyFuncTestCase.hash_size_instances:
            h1 = HashTable(upper)

            for k in MyFuncTestCase.key_instances:

                v = h1.hash(k)
                self.assertGreaterEqual(v, 0)
                self.assertLessEqual(v, int(upper)-1)

    def test_set_get(self):
        for hs in MyFuncTestCase.hash_size_instances:
            h1 = HashTable(hs)

            # check different key types
            with self.assertRaises(TypeError):
                for inst in MyFuncTestCase.non_string_instances:
                    h1.set(inst, inst)

            # do the set/get of some various typed values and check if the
            # value is set immediately after entry
            for inst in MyFuncTestCase.non_string_instances:
                h1.set(str(inst), inst)
                v = h1.get(str(inst))
                self.assertEqual(v, inst)

            # then, after all the values have been set, try to get them again
            for inst in MyFuncTestCase.non_string_instances:
                v = h1.get(str(inst))
                self.assertEqual(v, inst)

    def test_set_get_simple(self):
        # the value set for a key should have that value when retrieved
        for hs in MyFuncTestCase.hash_size_instances:
            h1 = HashTable(hs)
            h1.set("XYTZ", 1776)
            v = h1.get("XYTZ")
            self.assertEqual(v, 1776)

            for k in MyFuncTestCase.key_instances:
                h1.set(k, len(k))
                v = h1.get(k)
                self.assertEqual(v, len(k))

            for k in MyFuncTestCase.key_instances:
                v = h1.get(k)
                self.assertEqual(v, len(k))

    def test_set_get_latest(self):
        # the last entry for a key for a value should be the value
        h1 = HashTable(4)
        h1.set("A", 0)
        h1.set("A", 1)
        v = h1.get("A")
        self.assertEqual(v, 1)

    def test_set_get_collisions(self):
        # without knowing hash function details, this is the only way
        # to ensure keys will collide by setting the size of the table
        h1 = HashTable(1)
        h1.set("test", 1776)
        h1.set("table", 1783)

        v1 = h1.get("test")
        v2 = h1.get("table")

        self.assertEqual(v2, 1783)
        self.assertEqual(v1, 1776)

    def test_set_get_manywords(self):
        h1 = HashTable(10000)
        f = open('/usr/share/dict/words')

        if f is not None:
            for line in f:
                h1.set(line, 0)

            # now test get on all the words
            sum = 0
            for line in f:
                sum += h1.get(line)

            self.assertEqual(sum, 0)


if __name__ == "__main__":
    unittest.main()
