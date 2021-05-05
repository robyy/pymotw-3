#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
import array
import binascii

# the unit of hex number is 4 bits, 0x1111 = 16, so 2 hex number is 1 byte(8 bits)
# for number 12345678(int, 4 bytes in Python), in big-endian, it's stored as 0x12 0x34 0x56 0x78,
# in little-endian, it's stored as 0x78 0x56 0x34 0x12
def to_hex(a):
    chars_per_item = a.itemsize * 2  # 2 hex digits
    hex_version = binascii.hexlify(a)
    num_chunks = len(hex_version) // chars_per_item
    for i in range(num_chunks):
        start = i * chars_per_item
        end = start + chars_per_item
        yield hex_version[start:end]


start = int('0x12345678', 16)
print(start)
end = start + 5
a1 = array.array('i', range(start, end))
a2 = array.array('i', range(start, end))
a2.byteswap()

fmt = '{:>12} {:>12} {:>12} {:>12}'
print(fmt.format('A1 hex', 'A1', 'A2 hex', 'A2'))
print(fmt.format('-' * 12, '-' * 12, '-' * 12, '-' * 12))
fmt = '{!r:>12} {:12} {!r:>12} {:12}'
for values in zip(to_hex(a1), a1, to_hex(a2), a2):
    print(fmt.format(*values))

# The * operator can be used in conjunction with zip() to unzip the list.
temp = [('x', 3, 999), ('y', 4, 1000), ('z', 5, 1001)]
c, v, tt = zip(*temp)

print(c)
print(v)
print(tt)
