#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
import functools


def standalone(self, a=1, b=2):
    "Standalone function"
    print('  called standalone with:', (self, a, b))
    if self is not None:
        print('  self.attr =', self.attr)


class MyClass:
    "Demonstration class for functools"

    def __init__(self):
        self.attr = 'instance attribute'

    # partialmethod() returns a callable ready to be used as an unbound method of an object
    method1 = functools.partialmethod(standalone)
    method2 = functools.partial(standalone)


o = MyClass()

print('standalone')
standalone(None)
print()

# method1() can be called from an instance of MyClass, and the instance is passed as the first argument just
# as with methods defined normally.
print('method1 as partialmethod')
o.method1()
print()

# method2() is not set up as a bound method, and so the self argument must be
# # passed explicitly, or the call will result in a TypeError.
print('method2 as partial')
try:
    o.method2()
except TypeError as err:
    print('ERROR: {}'.format(err))

print('------')
o.method2(o)

print('------')


class Test(object):
    def method_one(self):
        print("Called method_one, bound method")

    # The decorator tells the built-in default metaclass type (the class of a class, cf. this question:
    # https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python) to
    # not create bound methods for method_two.
    # Now, you can invoke static method both on an instance or on the class directly:
    @staticmethod
    def method_two():
        print("Called method two, staticmethod")

    @classmethod
    def method_three(cls):
        print("Called method three, classmethod")
        print(cls)

    def method_four():
        print("Called method_four, unbound method")


a_test = Test()
# In Python, there is a distinction between bound and unbound methods.
# Basically, a call to a member function (like method_one), a bound function
# a_test.method_one() is translated to Test.method_one(a_test), i.e. a call to an unbound method
# the so-called bound, is just auto bind the object instance to the first argument self in the method
a_test.method_one()
a_test.method_two()
a_test.method_three()

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: method_two() takes no arguments (1 given)
a_test.method_four()
