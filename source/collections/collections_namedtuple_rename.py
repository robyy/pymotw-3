#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
import collections

# In situations where a namedtuple is created based on values outside the control of the program (such as to represent the rows returned by
# a database query, where the schema is not known in advance), the rename option should be set to True so the invalid fields are renamed.
with_class = collections.namedtuple(
    'Person', 'name class age',
    rename=True)
print(with_class._fields)

# The new names for renamed fields depend on their index in the tuple, so the field with name class becomes _1 and
# the duplicate age field is changed to _2.
two_ages = collections.namedtuple(
    'Person', 'name age age',
    rename=True)
print(two_ages._fields)
