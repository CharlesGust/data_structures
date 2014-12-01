import timeit

# Assignment

# Then create a new branch and implement the sort in a new file in your
#  data-structures repository.

# Add tests to the repository that demonstrate that it works correctly.

# In addition, add inline tests in an "if __name__ == '__main__':" block
#  that demonstrate the performance difference between best and worst-case
#  for the sort.

# Add information about your implementation into the README.md file,
#  including any sources or collaborators you used.
#
# I contribute to Wikipedia, and you should too.
#  Kudos to http://en.wikipedia.org/wiki/Quicksort
#
# Kudos to Ben Friedland for suggesting I read:
#  http://en.literateprograms.org/Quicksort_(Python)
# and to the folks running literateprograms.org
#


def quicksort_pivot(n):
    """ return the index of the element to pivot around with list of length n """
    return int(n/2)

def partition(unsorted, begin, end):
    """ return index where the pivot value was placed """
    pivot_index = begin + quicksort_pivot(end-begin+1)
    pivot_value = unsorted[pivot_index]

    # swap values at pivot_index and end - the end is a temporary
    #  holder for the pivot
    temp = unsorted[pivot_index];
    unsorted[pivot_index] = unsorted[end]
    unsorted[end] = temp

    # find out where to place the end value
    ripple_index = begin
    for i in xrange(begin, end):
        if unsorted[i] < pivot_value:
            # swap values at current index and ripple_index
            temp = unsorted[i]
            unsorted[i] = unsorted[ripple_index]
            unsorted[ripple_index] = temp

            ripple_index += 1

    # now retrieve the pivot value from the end and swap
    #  it with where the ripple found
    temp = unsorted[ripple_index]
    unsorted[ripple_index] = unsorted[end]
    unsorted[end] = temp
    return ripple_index


def sort_elements_inplace(unsorted, begin, end):
    if begin < end:
        pivot_index = partition(unsorted, begin, end)
        sort_elements_inplace(unsorted, begin, pivot_index-1)
        sort_elements_inplace(unsorted, pivot_index+1, end)


def sort(unsorted):
    """ quick sort of unsorted array """

    # if the list is zero or one element, it is already sorted
    if len(unsorted) <= 1:
        return unsorted

    sort_elements_inplace(unsorted, 0, len(unsorted)-1)
    return unsorted


def time_one(count, elementtext, xrangetext):
    count_text = str(count)
    timeitstr = 'arr=['+elementtext+' for i in xrange('+xrangetext+')]; sort(arr)'
    result = timeit.timeit(timeitstr, setup="from __main__ import sort; import random")
    print "Quick sort of {0} elements from {1} of xrange({2}) takes {3} seconds".format(
        count, elementtext, xrangetext, result)


if __name__=="__main__":

    for x in [2, 5, 10]:
        time_one(x, 'i', '0,{0}'.format(x))
        time_one(x, 'i', '{0},0,-1'.format(x))
        time_one(x, 'random.randrange(0,{0})'.format(x), '0,{0}'.format(x))
