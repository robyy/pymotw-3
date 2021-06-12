#!/usr/bin/env python3
# encoding: utf-8
"""
"""

# end_pymotw_header
import functools


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


class E(C, D):
    pass


@functools.singledispatch
def myfunc(arg):
    print('default myfunc({})'.format(arg.__class__.__name__))


@myfunc.register(A)
def myfunc_A(arg):
    print('myfunc_A({})'.format(arg.__class__.__name__))


@myfunc.register(B)
def myfunc_B(arg):
    print('myfunc_B({})'.format(arg.__class__.__name__))


@myfunc.register(C)
def myfunc_C(arg):
    print('myfunc_C({})'.format(arg.__class__.__name__))


# When no exact match is found for the type, the inheritance order is evaluated and the closest matching type is used.
myfunc(A())
myfunc(B())
myfunc(C())
myfunc(D())  # class D(B):, so the output is "myfunc_B(D)"
myfunc(E())  # class E(C, D):, so the output is "myfunc_C(E)"

print('---------')


class Mother:
    def __init__(self, a):
        self.a = a

    x = 'Class Var x Mother'


class Father:
    def __init__(self, a):
        self.a = a

    x = 'Class Var x Farther'


class Child(Mother, Father):
    pass


print(Child(99).x)  # Mother first met in MRO, so use mother.x
