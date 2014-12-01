#!/usr/bin/env python

"""
code that tests the SimpleGraph class defined in simple_graph.py

can be run with py.test
"""

import pytest  # used for the exception testing
import unittest

from simple_graph import Node, Edge


class MyFuncTestCase(unittest.TestCase):

    # g.nodes(): return a list of all nodes in the graph
    # g.edges(): return a list of all edges in the graph
    # g.add_node(n): adds a new node 'n' to the graph
    # g.add_edge(n1, n2): adds a new edge to the graph connecting 'n1' and 'n2', if either n1 or n2 are not already present in the graph, they should be added.
    # g.del_node(n): deletes the node 'n' from the graph, raises an error if no such node exists
    # g.del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from the graph, raises an error if no such edge exists
    # g.has_node(n): True if node 'n' is contained in the graph, False if not.
    # g.neighbors(n): returns the list of all nodes connected to 'n' by edges, raises an error if n is not in g
    # g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g

    def test_Node___init__(self):
        Node0 = Node(0)
        self.assertEqual(Node0.val, 0)
        self.assertIsNone(Node0.link)

    def test_IterNode(self):
        i1 = IterNode(None)
        self.assertIsNone(i1.cur)

        with self.assertRaises(StopIteration):
            i1.next()

        Node0 = Node(0)
        i2 = IterNode(Node0)
        self.assertIsNotNone(i2.cur)
        Node1 = i2.next()
        self.assertEqual(Node0, Node1)

        with self.assertRaises(StopIteration):
            i2.next()

    def test_LinkedList___init__(self):
        l1 = LinkedList()
        self.assertIsNone(l1.head)

    def test_LinkedList_insert(self):
        l1 = LinkedList()
        l1.insert(0)

        # ensure Node(0) added to list
        Node0 = l1.head
        self.assertEqual(Node0.val, 0)
        self.assertIsNone(Node0.link)

        # ensure Node(1) added to front of list
        l1.insert(1)
        Node1 = l1.head
        self.assertEqual(Node1.val, 1)
        self.assertIsNotNone(Node1.link)

        # ensure Node(0) is next in list
        Node0 = Node1.link
        self.assertEqual(Node0.val, 0)
        self.assertIsNone(Node0.link)

        # ensure adding 'None' adds something
        sz1 = l1.size()
        l1.insert(None)
        self.assertEqual(sz1+1, l1.size())

        # ensure adding recursively adds nothing
        sz1 = l1.size()
        l1.insert(l1)
        self.assertEqual(sz1, l1.size())

    def test_LinkedList_append(self):
        l1 = LinkedList()
        l1.append(0)

        # ensure Node(0) added to list
        Node0 = l1.head
        self.assertEqual(Node0.val, 0)
        self.assertIsNone(Node0.link)

        # ensure Node(1) appended to back of list
        l1.append(1)
        Node0 = l1.head
        self.assertEqual(Node0.val, 0)
        self.assertIsNotNone(Node0.link)

        # ensure Node(0) is next in list
        Node1 = Node0.link
        self.assertEqual(Node1.val, 1)
        self.assertIsNone(Node1.link)

        # ensure adding 'None' adds something
        sz1 = l1.size()
        l1.append(None)
        self.assertEqual(sz1+1, l1.size())

        # ensure adding recursively adds nothing
        sz1 = l1.size()
        l1.append(l1)
        self.assertEqual(sz1, l1.size())

    def test_LinkedList_pop(self):
        l1 = LinkedList()
        l1.insert(0)
        self.assertEqual(l1.size(), 1)
        l1.insert(1)
        self.assertEqual(l1.size(), 2)

        # ensure Node(0) added to list
        Val1 = l1.pop()
        self.assertEqual(l1.size(), 1)
        self.assertEqual(Val1, 1)

        Val0 = l1.pop()
        self.assertEqual(l1.size(), 0)
        self.assertEqual(Val0, 0)

        # if the list is empty and you pop, raise ValueError
        with self.assertRaises(ValueError):
            ValNone = l1.pop()

    def test_LinkedList_size(self):
        l1 = LinkedList()
        self.assertEqual(l1.size(), 0)
        l1.insert(0)
        self.assertEqual(l1.size(), 1)
        l1.insert(1)
        self.assertEqual(l1.size(), 2)
        l1.insert(2)
        self.assertEqual(l1.size(), 3)
        l1.remove_val(2)
        self.assertEqual(l1.size(), 2)
        l1.remove_val(0)
        self.assertEqual(l1.size(), 1)
        l1.remove_val(1)
        self.assertEqual(l1.size(), 0)

    def test_LinkedList_search(self):
        l1 = LinkedList()
        l1.insert(0)
        l1.insert(1)
        l1.insert(2)
        Node2 = l1.search(2)
        self.assertEqual(Node2.val, 2)
        Node0 = l1.search(0)
        self.assertEqual(Node0.val, 0)
        Node1 = l1.search(1)
        self.assertEqual(Node1.val, 1)

    def test_LinkedList_remove(self):
        l1 = LinkedList()
        l1.insert(0)
        l1.insert(1)
        l1.insert(2)

        Node3 = Node(3)
        with self.assertRaises(ValueError):
            l1.remove(Node3)
            l1.remove_val(3)

        self.assertEqual(l1.size(), 3)
        Node2 = l1.search(2)
        l1.remove(Node2)
        self.assertEqual(l1.size(), 2)
        Node0 = l1.search(0)
        l1.remove(Node0)
        self.assertEqual(l1.size(), 1)
        Node1 = l1.search(1)
        l1.remove(Node1)
        self.assertEqual(l1.size(), 0)

        with self.assertRaises(ValueError):
            l1.remove(Node1)
            l1.remove(Node0)
            l1.remove(Node2)
            l1.remove_val(1)
            l1.remove_val(0)
            l1.remove_val(2)

    def test_LinkedList___repr__(self):
        l1 = LinkedList()
        l1.insert(0)
        l1.insert(1)
        l1.insert(2)

        self.assertEquals(l1.__repr__(), "(2, 1, 0)")

if __name__ == "__main__":
    unittest.main()
