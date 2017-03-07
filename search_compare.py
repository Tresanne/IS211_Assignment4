#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Working with Algorithms"""

import time
from timeit import Timer
import random


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    return found, end-start


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    return found, end-start


def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    return found, end-start


def binary_search_helper(a_list, item):
    if len(a_list) == 0:
        return False, time.time()
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True, time.time()
        else:
            if item < a_list[midpoint]:
                return binary_search_helper(a_list[:midpoint], item)
            else:
                return binary_search_helper(a_list[midpoint + 1:], item)


def binary_search_recursive(a_list, item):
    start = time.time()
    found, end = binary_search_helper(a_list, item)
    return found, end-start


def main():
    total_time = 0.00
    for _ in range(100):
        sample = random.sample(xrange(1000), 500)
        total_time += sequential_search(sample, -1)[1]
    print "Sequential search took %10.7f seconds to run on average" % (
        total_time/100.00)

    total_time = 0.00
    for _ in range(100):
        sample = random.sample(xrange(1000), 500)
        sample.sort()
        total_time += ordered_sequential_search(sample, -1)[1]
    print "Ordered sequential search took %10.7f seconds to run on average" % (
        total_time/100.00)

    total_time = 0.00
    for _ in range(100):
        sample = random.sample(xrange(1000), 500)
        sample.sort()
        total_time += binary_search_iterative(sample, -1)[1]
    print "Iterative binary search took %10.7f seconds to run on average" % (
        total_time/100.00)

    total_time = 0.00
    for _ in range(100):
        sample = random.sample(xrange(1000), 500)
        sample.sort()
        total_time += binary_search_recursive(sample, -1)[1]
    print "Recursive binary search took %10.7f seconds to run on average" % (
        total_time/100.00)

if __name__ == '__main__':
    main()
