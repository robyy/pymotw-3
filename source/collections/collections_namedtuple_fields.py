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
print('Representation:', bob)

# namedtuple provides several useful attributes and methods for working with subclasses and instances. All of these built-in properties
# have names prefixed with an underscore (_), which by convention in most Python programs indicates a private attribute. For namedtuple,
# however, the prefix is intended to protect the name from collision with user-provided attribute names.
print('Fields:', bob._fields)
