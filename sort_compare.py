#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 4 Search Module"""

import time
import random


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
    return end - start


def gap_insertion_sort(alist, start, gap):
    for x in range(start + gap, len(alist), gap):
        current_value = alist[x]
        position = x
        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = current_value


def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    return end - start


def python_sort(alist):
    start = time.time()
    alist = alist.sort()
    end = time.time()
    return end - start


def random_lists(listsize):
    my_randoms = []
    for i in range(listsize):
        my_randoms.append(random.randrange(1,listsize))
    return my_randoms


def main():
    timed_lists = [500, 1000, 10000, 50000, 100000]

    for i in timed_lists:
        insertion_sort_time = 0
        shell_sort_time = 0
        python_sort_time = 0
        counter = 100
        test_list = random_lists(i)
        while counter > 0:
            insertion_sort_time += insertion_sort(test_list)
            shell_sort_time += shell_sort(test_list)
            python_sort_time += python_sort(test_list)
            counter -= 1
        print 'List Length: ' + str(i)
        print ('The insertion sort took %10.9f' % (insertion_sort_time / 100) + ' to run, on average')
        print ('The shell sort took %10.9f' % (shell_sort_time / 100) + ' to run, on average')
        print ('The python sort took %10.9f' % (python_sort_time / 100) + ' to run, on average')

if __name__ == '__main__':
    main()