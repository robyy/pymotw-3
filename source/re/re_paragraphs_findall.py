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

# pattern fails for paragraphs at the end of the input text, as illustrated by the fact that “Paragraph three.” is not part of the output.
# Extending the pattern to say that a paragraph ends with two or more newlines or the end of input fixes the problem, but makes the pattern
# more complicated. Converting to re.split() instead of re.findall() handles the boundary condition automatically and keeps the pattern
# simpler.
for num, para in enumerate(re.findall(r'(.+?)\n{2,}',
                                      text,
                                      flags=re.DOTALL)
                           ):
    print(num, repr(para))
    print(num, para)
    print()
