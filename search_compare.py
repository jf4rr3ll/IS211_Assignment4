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
    return found, 'This function took ' + str('%.10f' % (end-start)) + ' seconds to run.'

test_list = [1,2,3,4,5,6,7,8,9]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 13))

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
    return found, 'This function took ' + str('%.10f' % int(end-start)) + ' seconds to run.'

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list, 13))


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

    return found, 'This function took ' + str('%.10f' % int(end - start)) + ' seconds to run.'


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

def random_lists():
    my_randoms = []
    for i in range (500):
        my_randoms.append(random.randrange(1,500,1))
    return my_randoms

print(sequential_search(my_randoms, -1))
print(ordered_sequential_search(my_randoms, -1))