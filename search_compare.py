#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 4 Search Module"""

import time
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
    return found, end - start


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item: found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    end = time.time()
    return found, end - start


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
    return found, end - start


def binary_search_recursive(a_list, item):
    start = time.time()
    if len(a_list) == 0:
        end = time.time()
        return False, end - start
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            end = time.time()
            return True, end - start
        else:
            if item < a_list[midpoint]:
                end = time.time()
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                end = time.time()
                return binary_search_recursive(a_list[midpoint + 1:], item)

def random_lists(listsize):
    my_randoms = []
    for i in range(listsize):
        my_randoms.append(random.randrange(1,listsize))
    return my_randoms


def main():
    timed_lists = [500, 1000, 10000, 50000, 100000]

    for i in timed_lists:
        sequential_search_time = 0
        ordered_seq_search_time = 0
        binary_iterative_search_time = 0
        binary_recursive_search_time = 0
        counter = 100
        test_list = random_lists(i)
        while counter > 0:
            sequential_search_time += sequential_search(test_list, -1)[0]
            ordered_seq_search_time += ordered_sequential_search(test_list, -1)[0]
            binary_iterative_search_time += binary_search_iterative(test_list, -1)[0]
            binary_recursive_search_time += binary_search_recursive(test_list, -1)[0]
            counter -= 1
        print 'List Length: ' + str(i)
        print ('The sequential search took %10.9f' % (sequential_search_time / 100) + ' to run, on average')
        print ('The ordered sequential search took %10.9f' % (ordered_seq_search_time / 100) + ' to run, on average')
        print ('The iterative binary search took %10.9f' % (binary_iterative_search_time / 100) + ' to run, on average')
        print ('The recursive binary search took %10.9f' % (binary_recursive_search_time / 100) + ' to run, on average')

if __name__ == '__main__':
    main()