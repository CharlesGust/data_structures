#!/usr/bin/env python

def insert_mid(tree, num, step):
    tree.insert(num)
    if step == 0:
        return
    print "inserting %d" % num

    insert_mid(tree, num+step, int(step/2))

    insert_mid(tree, num-step, int(step/2))


def insert_span(tree, span):
    insert_mid(tree, span/2, span/4)


if __name__=="__main__":
    # worst case: inserting values in increasing or decreasing order
    #  results in a linked list, O(n) to search
    bst1 = BinarySearchTree()
    bst2 = BinarySearchTree()

    for i in xrange(100):
        bst1.insert(i)
        bst2.insert(100-i)

    if bst1.depth() == 100:
        print "Worst Case: in order insert performs as linked list"
    if bst2.depth() == 100:
        print "Worst Case: reverse order insert performs as linked list"

    # Best Case: inserting values with middle value first, then middle
    #  of top section and bottom section.
    bst3 = BinarySearchTree()

    insert_span(bst3, 256)

    print "Best Case: inserting at mids has depth %d" % bst3.depth()
