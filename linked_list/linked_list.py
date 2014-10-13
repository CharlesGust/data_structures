class Node():
    def __init__(self, val, link=None):
        self.val = val
        self.link = link


class IterNode():
    def __init__(self, head):
        self.cur = head

    def __iter__(self):
        return self

    def next(self):
        if self.cur is not None:
            ret = self.cur
            self.cur = self.cur.link
            return ret
        else:
            raise StopIteration


class LinkedList():
    """ implement linked_list class. Uses None for invalid values, which
        implies None may not be stored in the list
    """
    def __init__(self):
        self.head = None

    def insert(self, val):
        """ insert the value 'val' at the head of the list """
        if val is None:
            return

        if val is self:
            """
            This is a simple check to eliminate the most obvious recursion
            but to truly detect recursion would require at least an O(n)
            search on every insert().

            if recursion is built into the linked list a runtime
            error will result when __repr__ is called.
            """
            return
        self.head = Node(val, self.head)
        return

    def append(self, val):
        """ append the value 'val' at the end of the list """
        if val is None:
            return

        if val is self:
            """
            This is a simple check to eliminate the recursion when the
            val in the append() is the list
            """
            return
        prev = None
        for cur in IterNode(self.head):
            if cur is val:
                """
                Since this walks to the end of the list anyway
                check if a recursion is being created by append()
                """
                return
            prev = cur

        new_node = Node(val)
        if prev is None:
            self.head = new_node
        else:
            prev.link = new_node

    def pop(self):
        """ pop the first value off the head of the list and return it. """
        if self.head is None:
            """ list is empty """
            return None
        val = self.head.val
        self.head = self.head.link
        return val

    def size(self):
        """ return the length of the list """
        sz = 0
        for cur in IterNode(self.head):
            sz += 1
        return sz

    def search(self, val):
        """ return the node containing 'val' in the list, if present, else None """
        for cur in IterNode(self.head):
            if cur.val == val:
                return cur
        return None

    def span_link(self, prev, cur):
        if prev is None:
            self.head = cur.link
        else:
            prev.link = cur.link
        return cur.link

    def remove_val(self, val):
        """ remove the given value from the list, wherever it might be (value must be an item in the list """
        prev = None

        for cur in IterNode(self.head):
            if cur.val == val:
                return self.span_link(prev, cur)
            prev = cur
        """ could just return, but spec says it must be in list """
        raise ValueError

    def remove(self, node):
        """ remove the given node from the list, wherever it might be (node must be an item in the list """
        prev = None

        for cur in IterNode(self.head):
            if cur == node:
                return self.span_link(prev, cur)
            prev = cur
        """ could just return, but spec says it must be in list """
        raise ValueError

    def __repr__(self):
        """ display the list represented as a Python tuple literal: "(12, 'sam', 37, 'tango')"
        """

        s1 = "("
        for cur in IterNode(self.head):
            s1 += cur.val.__repr__()
            if cur.link is not None:
                s1 += ", "
        s1 += ")"
        return s1

    def display(self):
        """ display the linked list; cannot name this method print """
        print self.__repr__()
