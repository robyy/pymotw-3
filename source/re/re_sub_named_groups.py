#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Substitute based on patterns.
"""

#end_pymotw_header
import re

bold = re.compile(r'\*{2}(?P<bold_text>.*?)\*{2}')

text = 'Make this **bold**.  This **too**.'

print('Text:', text)
print('Bold:', bold.sub(r'<b>\g<bold_text></b>', text))

# The \g<name> syntax also works with numbered references, and using it eliminates any ambiguity between group numbers and surrounding
# literal digits.
print('Bold:', bold.sub(r'<b>\g<1></b>', text))
