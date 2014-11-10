import sys

sys.path.insert(0, "../linked_list")
from ..linked_list.linked_list import LinkedList

class Stack(LinkedList):
    def push(self, val):
        LinkedList.insert(self, val)

    """
    certain functions from LinkedList could be implemented from the
    base class, but they are being overridden to raise exceptions
    because the classic interface of a stack would not permit these

    the size() method is not being overridden
    """
    def remove(*arg, **kwargs):
        raise NotImplementedError

    def remove_val(*arg, **kwargs):
        raise NotImplementedError

    def search(*arg, **kwargs):
        raise NotImplementedError

    def insert(*arg, **kwargs):
        raise NotImplementedError
