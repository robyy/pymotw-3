#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
import collections
import inspect

# namedtuple instances are just as memory efficient as regular tuples because they do not have per-instance dictionaries.
# Each kind of namedtuple is represented by its own class, which is created by using the namedtuple() factory function.

Person = collections.namedtuple('Person', 'name age')
# Person = collections.namedtuple('Person', ['name', 'age'])
# Person = collections.namedtuple('Person', ('name', 'age'))

print(Person)

bob = Person(name='Bob', age=30)
print('\nRepresentation:', bob)

print('---------')
print(inspect.getmro(Person))  # (<class '__main__.Person'>, <class 'tuple'>, <class 'object'>)
print(type(Person))  # <class 'type'>, Person is a type object, a class
print(type(bob))  # <class '__main__.Person'>
# >>> type(int)
# <type 'type'>
# >>> type(1)
# <type 'int'>
#
# >>> class Foo(object):
#     ...   pass
# >>> type(Foo)
# <type 'type'>
# >>> obj = Foo()
# >>> type(obj)
# <class '__main__.Foo'>
print('---------')

jane = Person(name='Jane', age=29)
print('\nField by name:', jane.name)

print('\nFields by index:')
for p in [bob, jane]:
    print('{} is {} years old'.format(*p))  # namedtuple can be unpacked as well
    print('{} is {} years old'.format(p[0], p[1]))
