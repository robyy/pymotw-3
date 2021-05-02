#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import collections

Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('\nBefore:', bob)
# Although the name implies it is modifying the existing object, because namedtuple instances are immutable the method actually returns
# a new object.
bob2 = bob._replace(name='Robert')
print('After:', bob2)
print('Same?:', bob is bob2)
