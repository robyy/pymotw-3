#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Match email addresses
"""

#end_pymotw_header
import re

address = re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)')

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
]

for candidate in candidates:
    match = address.search(candidate)
    print('{:<30}  {}'.format(
        candidate, 'Matches' if match else 'No match')
    )
    # print(f"{candidate:<30}        {'Matches' if match else 'No match'}")

print('--------------')
candidates2 = [
    'first.last@example.com',
    'first.last+category@gmail.com',
    'valid-address@mail.example.com',
    'not-valid@example.foo',
]

for candidate in candidates2:
    match = address.search(candidate)
    print('{:<30}  {}'.format(
        candidate, 'Matches' if match else 'No match')
    )
