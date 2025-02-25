#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
from operator import *

# The functions in the operator module work via the standard Python interfaces when performing their operations.
# Thus, they work with user-defined classes as well as the built-in types.
class MyObj:
    """Example for operator overloading"""

    def __init__(self, val):
        # super(MyObj, self).__init__()
        self.val = val

    def __str__(self):
        return 'MyObj({})'.format(self.val)

    def __lt__(self, other):
        """compare for less-than"""
        print('Testing {} < {}'.format(self, other))
        return self.val < other.val

    def __add__(self, other):
        """add values"""
        print('Adding {} + {}'.format(self, other))
        return MyObj(self.val + other.val)


a = MyObj(1)
b = MyObj(2)

print('Comparison:')
print(lt(a, b))

print('\nArithmetic:')
print(add(a, b))

# is and == comparison
print('-------is and == comparison---------')
p = 999
w = 999
print(p is w)
