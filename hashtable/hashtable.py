#!usr/bin/python

#
# hashtable.py
#
# For the purposes of this assignment, it uses a naive hashing function, one
# that sums the ordinal values of the characters in a key and uses the
# modulus operator to fold the result into one of the available container
# indexes in the table.

# The table has the following properties:
#
#     It is fixed size.  The number of slots in the table is determined
#      when the table is initialized, by passing an argument:
#        foo = HashTable(1024)
#     It handles hash collisions by using 'buckets' to contain any values
#      that share a hash
#     It accepts only strings as keys.  If a non-string is provided, the
#      'set' method raises an appropriate Python exception.
#     It should implement the following methods:
#         get(key) - should return the value stored with the given key
#         set(key, val) - should store the given val using the given key
#         hash(key) - should hash the key provided


class HashTable():
    def __init__(self, slots=1024):
        """ initialize HashTable with positive number of 'int' slots """
        if type(slots) != int:
            raise TypeError("HashTable size must be of type 'int'")

        if slots <= 0:
            raise IndexError("HashTable size must be positive 'int'")

        self.slots = slots
        self.table = []

        for i in xrange(slots):
            self.table.append([])
        return

    def hash(self, key):
        """ return hash value by adding the ordinal value of each character """

        hashval = 0

        for character in key:
            hashval += ord(character)

        return hashval % self.slots

    def get(self, key):
        """ return value associated with key """
        keyvaluelist = self.table[self.hash(key)]

        for entry in keyvaluelist:
            if entry[0] == key:
                return entry[1]

        raise KeyError("{0}".format(key))
        return

    def set(self, key, val):
        """ set key to value and place in HashTable """
        if type(key) is not str:
            raise TypeError("HashTable key must be type 'str'")

        keyvaluelist = self.table[self.hash(key)]

        # if key already seen, just update value
        for entry in keyvaluelist:
            if entry[0] == key:
                entry[1] = val
                return

        # if key not yet in hash table, append to this keylist
        keyvaluelist.append([key, val])
        return

