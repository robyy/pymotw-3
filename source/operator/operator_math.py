#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

#end_pymotw_header
from operator import *

a = -1
b = 5.0
c = 2
d = 6

print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)

print('\nPositive/Negative:')
print('abs(a):', abs(a))
print('neg(a):', neg(a))
print('neg(b):', neg(b))
print('pos(a):', pos(a))  # Same as +a
print('pos(b):', pos(b))

print('\nArithmetic:')
print('add(a, b)     :', add(a, b))
print('floordiv(a, b):', floordiv(a, b))
print('floordiv(d, c):', floordiv(d, c))
print('mod(a, b)     :', mod(a, b))  # Same as a % b.
print('mul(a, b)     :', mul(a, b))
print('pow(c, d)     :', pow(c, d))
print('sub(b, a)     :', sub(b, a))
print('truediv(a, b) :', truediv(a, b))
print('truediv(d, c) :', truediv(d, c))

print('\nBitwise:')
print('and_(c, d)  :', and_(c, d))

# c = 2 = 0000 0010, ~c = 1111 1101, it's twos' complement, so convert it to ones' complement:
# 1111 1101 - 1 = 1111 1100, then convert it to sign-magnitude:
# 1000 0011 = -3
print('invert(c)   :', invert(c))  # Same as ~c.

# >>>: unsigned right shift or a zero-fill right shift
# >>: signed right shift, maintains the sign of a number by replicating its sign bit before moving bits to the right
# 2 << 6 = 0000 0000 0010 << 6 = 0000 1000 0000 = 128
# in python 3 the plain int type is unbounded.
# https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
print('lshift(c, d):', lshift(c, d))
print('or_(c, d)   :', or_(c, d))
print('rshift(d, c):', rshift(d, c))
print('xor(c, d)   :', xor(c, d))


print('-----')
print(1 % 5)
# The modulo operator always yields a result with the same sign as its second operand (or zero);
# the absolute value of the result is strictly smaller than the absolute value of the second operand
# The function math.fmod() returns a result whose sign matches the sign of the first argument instead
print(-1 % 5)  # a%b = a - (a/b) * b = -1 - (-1/5) * 5 = -1 - (-1) * 5 = -1 + 5 = 4
print(-1 % 5.0)  # 4.0
print(-9 % 5)

# 已知 a, b(b not equal 0 ) 是整数，求 a % b, (a 或 b 为负数)
# a = q * b + r
#   = (a/b) * b + a%b
#
# 所以，
#
# a%b = a - (a/b) * b
#
# 所以关键就是 a/b 如何取整的问题。
#
# 口算 / 计算器 / Python：向下取整（往小了取）
#
# C/C++/Java：向零取整（直接把小数部分去掉）

# 原码(Sign-Magnitude)，反码(ones' Complement)，补码(two's Complement) 详解
# https://www.cnblogs.com/zhangziqiu/archive/2011/03/30/computercode.html

