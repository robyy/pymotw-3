#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Splitting input based on a pattern.
"""

#end_pymotw_header
import re

text = '''Paragraph one
on two lines.

Paragraph two.


Paragraph three.'''

print('With split:')
for num, para in enumerate(re.split(r'(\n{2,})', text)):
    print(num, repr(para))
    print()


print('str.partition():')
# output: Tuple ('Paragraph one\non two lines.', '\n\n', 'Paragraph two.\n\n\nParagraph three.')
print(text.partition('\n\n'))
# raw string treats \n as literal \n instead of new line

print()
print('str.splitlines()')
# output: List ['Paragraph one', 'on two lines.', '', 'Paragraph two.', '', '', 'Paragraph three.']
print(text.splitlines())
