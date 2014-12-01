import timeit

# Assignment

# Then create a new branch add an implementation of this algorithm
#  to your data-structures repository.  Make a variety that works for
#  sorting positive integers and another that works for string values.

# Add tests to demonstrate that the algorithm works properly.

# Add an "if __name__ == '__main__':" block that contains code
#  demonstrating the performance of the sort in best- and worst-case
#  situations across a variety of input sizes.

# Add information about your implementations to the README.md file,
#  including sources and collaborations used.

# I contribute to Wikipedia, and you should too.
#  Kudos to http://en.wikipedia.org/wiki/Radix_sort
#
#


def get_right_char(val, base, k, maxlen):
    """ return if val has kth character and the kth character from the right """
    this_one_done = (k >= maxlen-1)
    retval = ' ' if (maxlen-k > len(val)) else val[maxlen-k-1]
    return this_one_done, ord(retval)


def get_right_digit(val, base, k, maxlen):
    """ return if val has kth digit and the kth digit from the right """
    highdigits = (val // base ** k)
    this_one_done = (highdigits == 0)
    # if this_one_done:
    #     print "This one done {}, {}, {}".format(val, base, k)
    return this_one_done, (highdigits % base)


def clear_buckets(n):
    return [[] for _ in xrange(n)]


def bucketize_list(unsorted, getkth, slots, k, maxlen):
    buckets = clear_buckets(slots)
    all_done = True
    for i in unsorted:
        this_one_done, index = getkth(i, slots, k, maxlen)
        all_done = all_done and this_one_done
        buckets[index].append(i)
    # print "All done? {}, buckets {}".format(all_done, buckets)
    return all_done, buckets


def unbucketize_list(buckets):
    unsorted = []
    for i in buckets:
        unsorted.extend(i)
    # print unsorted
    return unsorted


def sort(unsorted, slots, getkth, maxlen=0):
    # copy_list = list(unsorted)
    if len(unsorted) <= 1:
        return unsorted

    all_done = False
    k = 0
    while not all_done:
        all_done, buckets = bucketize_list(unsorted, getkth, slots, k, maxlen)
        # print "in sort(): all_done={}, buckets={}".format(all_done, buckets)
        unsorted = unbucketize_list(buckets)
        # print "in_sort(): unsorted={}".format(unsorted)
        k += 1

    return unsorted


def sorti(unsorted):
    return sort(unsorted, 10, get_right_digit)


def sorts(unsorted):
    maxlen = max(len(s) for s in unsorted)

    return sort(unsorted, 256, get_right_char, maxlen)


def time_one(count, elementtext, xrangetext):

    timeitstr =\
        'arr=['+elementtext+' for i in xrange('+xrangetext+')]; sorti(arr)'

    result = timeit.timeit(
        timeitstr,
        setup="from __main__ import sorti; import random"
        )

    print "Radix sort of {0} elements from {1} of xrange({2}) takes {3} seconds"\
        .format(count, elementtext, xrangetext, result)


if __name__ == "__main__":

    for x in [2, 5, 10]:
        time_one(x, 'i', '0,{0}'.format(x))
        time_one(x, 'i', '{0},0,-1'.format(x))
        time_one(x, 'random.randrange(0,{0})'.format(x), '0,{0}'.format(x))
