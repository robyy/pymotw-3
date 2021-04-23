#!/usr/bin/env python3
# encoding: utf-8
"""
"""

# end_pymotw_header
import enum

BugStatus = enum.Enum(
    value='BugStatusbbbbbbbb',
    names=('fix_released fix_committed in_progress '
           'wont_fix invalid incomplete new'),
)

print('Member: {}'.format(BugStatus.new))  # output: Member: BugStatusbbbbbbbb.new

print('\nAll members:')
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))

print()
print(dir(BugStatus))
print(BugStatus.__dict__)
