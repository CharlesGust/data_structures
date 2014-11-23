import timeit

# Assignment

# When you're ready, create a new branch for your data-structures repository
#  and add a module to implement the sorting algorithm.

# Include an "if __name__ == '__main__':" block at the end of your module that
#  demonstrates the performance characteristics of this sort over a variety of
#  lengths of input in both the best and worst-case scenarios. Executing your
#  module should print informative output about the performance of your sort to
#  the terminal.

# Add tests to demonstrate that the sorting algorithm works.

# Add information about your implementation to the README.md in your package,
#  including any sources and collaborations you used in creating it.

def sort(unsorted):
    """ insertion sort of unsorted array """

    # if the list is zero or one element, it is already sorted
    if len(unsorted) <= 1:
        return unsorted

    for n in xrange(1, len(unsorted)):
        # pick the nth element, and if it's value is less than any of the
        #  (already sorted) values in front of it, move it to the front
        for test_index in xrange(n, 1, -1):
            if unsorted[test_index] < unsorted[test_index-1]:
                val = unsorted[test_index-1]
                unsorted[test_index] = unsorted[test_index-1]
                unsorted[test_index-1] = val
            else:
                break

    # unsorted array is now sorted (was done in place with swaps)
    return unsorted

if __name__=="__main__":
    print timeit.timeit(sort([i for i in xrange(10000, 0, -1)]))
