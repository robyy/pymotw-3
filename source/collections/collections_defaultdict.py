#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Initializing a defaultdict.
"""

# end_pymotw_header
import collections


# CHECK https://docs.python.org/3.9/library/collections.html#collections.defaultdict.default_factory !
def default_factory():
    return 'default value'


# If default_factory is not None, it is called without arguments to provide a default value for the given key,
# this value is inserted in the dictionary for the key, and returned.
d = collections.defaultdict(default_factory, foo='bar')
print('d:', d)
print('foo =>', d['foo'])
print('bar =>', d['bar'])

print('----------')

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Using list(function/constructor name) as the default_factory, it is easy to group a sequence of key-value pairs into a
# dictionary of lists, can also use other constructor like set, int, str to return default value of those type, like int() is 0, str() is ''
d = collections.defaultdict(list)  # content/dict part of d is now empty: {}
print(d)

# This technique is simpler and faster than an equivalent technique using dict.setdefault():
for k, v in s:
    print(k, v)
    # d is originally empty, so d[k] has no value, will invoke default_factory(list here) to return a default value for d[k],
    # here is an empty list, so after d['yellow'].append(1), d is defaultdict(<class 'list'>, {'yellow': [1],})
    d[k].append(v)

print(d)
print(sorted(d.items()))
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

# output: 0
print(int())
s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
    d[k] += 1

print(sorted(d.items()))  # [('i', 4), ('m', 1), ('p', 2), ('s', 4)]


# Lamda is just one line anonymous function
# Useful when writing function inside function
# it can take multiple arguments but computes only one expression
# Syntax:
# x = lambda arguments : expression

# add = lambda a, b : a + b
# add(3,6) ## 9
print('-----------')
def constant_factory(value):
    return lambda: value  # closure


# first argument must be callable or None
d = collections.defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print(d)
# object is not defined, so it will use default_factory(lambda: value/'<missing>' here) to get a default value which is '<missing>'
print('%(name)s %(action)s to %(object)s' % d)
print(f'{d["name"]} {d["action"]} to {d["object"]}')
# NOTICE: output is still: John ran to <missing>, since d is defaultdict
print(f'{d["name"]} {d["action"]} to {d.get("object", "mMMMMissSSSing")}')

print(f'{d["name"]} {d["action"]} to {dict().get("object", "mMMMMissSSSing")}')
