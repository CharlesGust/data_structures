import timeit

# Assignment

# Then create a new branch and implement the algorithm in a new file in
#  your data-structures repository

# Include tests that demonstrate that your sort works correctly.

# Include inline tests in an "if __name__ == '__main__':" block that
#  demonstrate the difference between best and worst case performance
#  for this algorithm across a variety of input sizes.

# Add information about your implementation to your README.md file,
#  including any sources and collaborations used in creating it.
#
# I contribute to Wikipedia, and you should too.
#  Kudos to http://en.wikipedia.org/wiki/Merge_sort
#
def merge(left, right):
    result = []

    while True:
        if len(right) == 0:
            result.extend(left)
            return result
        if len(left) == 0:
            result.extend(right)
            return result
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)


def sort(unsorted):
    """ merge sort of unsorted array """

    # if the list is zero or one element, it is already sorted
    if len(unsorted) <= 1:
        return unsorted

    # divide the list into two virtually equal sized sub-lists and
    #  recursively sort each of them
    cut = int(len(unsorted) / 2)
    left = sort(list(unsorted[0:cut]))
    right = sort(list(unsorted[cut:]))

    return merge(left, right)


def time_one(count, elementtext, xrangetext):
    count_text = str(count)
    timeitstr = 'arr=['+elementtext+' for i in xrange('+xrangetext+')]; sort(arr)'
    result = timeit.timeit(timeitstr, setup="from __main__ import sort; import random")
    print "Merge sort of {0} elements from {1} of xrange({2}) takes {3} seconds".format(
        count, elementtext, xrangetext, result)


if __name__=="__main__":

    for x in [1, 2, 5, 10]:
        time_one(x, 'i', '0,{0}'.format(x))
        time_one(x, 'i', '{0},0,-1'.format(x))
        time_one(x, 'random.randrange(0,{0})'.format(x), '0,{0}'.format(x))
