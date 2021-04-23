#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2015 Doug Hellmann.  All rights reserved.
#
"""ChainMap as a namespace stack
"""

# end_pymotw_header
import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
c = {'c': 'E'}

m1 = collections.ChainMap(a, b)
# This is the equivalent of m2 = collections.ChainMap(c, *m1.maps), the *m1.maps unpacks the items of list as positional arguments which
# will resolve to m2 = collections.ChainMap(c, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
m2 = m1.new_child(c)

print('m1["c"] = {}'.format(m1['c']))
print('m2["c"] = {}'.format(m2['c']))

print(m1)
print(m2)

print('-------')
print(m1.maps)  # [{'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'}]
print(*m1.maps)  # {'a': 'A', 'c': 'C'} {'b': 'B', 'c': 'D'}
print(*m1.maps[0])  # a c
print(*m1.maps[1])  # b c
print(*(m1.maps[1]))  # b c, un pack the keys of dict: {'b': 'B', 'c': 'D'}

print('--------')

# A Python program to demonstrate both packing and
# unpacking.

# A sample python function that takes three arguments
# and prints them
def fun1(a, b, c):
    print(a, b, c)


# Another sample function.
# This is an example of PACKING. All arguments passed
# to fun2 are packed into tuple *args.
def fun2(*args):
    # Convert args tuple to a list so we can modify it
    args = list(args)

    # Modifying args
    args[0] = 'Geeksforgeeks'
    args[1] = 'awesome'

    # UNPACKING args and calling fun1()
    fun1(*args)


# Driver code
fun2('Hello', 'beautiful', 'world!')

print('-----------')
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print()
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits
# below also works, change fruits to list also works
# green, *tropic, red = fruits
# [green, *tropic, red] = fruits

print(green)
print(tropic)  # ['mango', 'papaya', 'pineapple']
print(red)

d = {'a': 'aaa', 'b': 'bbbb', 'ccc': 'ccccc'}
print(type(d.keys()))  # <class 'dict_keys'>

t1, t2, t3 = d  # unpack dict keys
print(t1, t2, t3)
