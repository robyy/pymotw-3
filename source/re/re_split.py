#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Splitting input based on a pattern.
"""

# end_pymotw_header
import re

text = '''Paragraph one
on two lines.

Paragraph two.


Paragraph three.'''

print('With findall:')
# a paragraph ends with two or more newlines or the end of input
# notice the combination of non-greedy repetition: (.+?) and re.DOTALL flag. re.DOTALL recognizes \n, non-greedy makes \n{2,} work
for num, para in enumerate(re.findall(r'(.+?)(\n{2,}|$)',
                                      text,
                                      flags=re.DOTALL)):
    print(num, repr(para))
    print()

print()
print('With split:')
for num, para in enumerate(re.split(r'\n{2,}', text)):
    print(num, repr(para))  # notice use repr here instead of para str.
    print()

# findall output: [('Paragraph one\non two lines.', '\n\n'), ('Paragraph two.', '\n\n\n'), ('Paragraph three.', '')] which contains group
print(re.findall(r'(.+?)(\n{2,}|$)',
                 text,
                 flags=re.DOTALL))

# output: ['Paragraph one\non two lines.', 'Paragraph two.', 'Paragraph three.']
print(re.split(r'\n{2,}', text))
