#!/usr/bin/env python
# -*- coding: utf-8 -*-
"Sort algorithms"

import random
import time

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    end = time.time()
    return a_list, end-start


def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        # print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2
    end = time.time()
    return a_list, end-start


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def python_sort(a_list):
    start = time.time()
    a_list.sort()
    end = time.time()
    return a_list, end-start


def main():

    total_time = 0.00
    for _ in range(100):
        sample = random.sample(xrange(1000), 500)
        total_time += insertion_sort(sample)[1]
    print "Insertion sort took %10.7f seconds to run on average" % (
        total_time/100.00)

    total_time = 0.00
    for _ in range(100):
        sample = random.sample(xrange(1000), 500)
        total_time += shell_sort(sample)[1]
    print "Shell sort took %10.7f seconds to run on average" % (
        total_time/100.00)

    total_time = 0.00
    for _ in range(100):
        sample = random.sample(xrange(1000), 500)
        total_time += python_sort(sample)[1]
    print "Python sort took %10.7f seconds to run on average" % (
        total_time/100.00)

if __name__ == '__main__':
    main()

