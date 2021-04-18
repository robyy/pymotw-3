#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""ID-based conditional expressions
"""

#end_pymotw_header
import re

# The syntax for testing whether a group has matched is (?(id)yes-expression| no-expression), where id is the group name or number,
# yes-expression is the pattern to use if the group has a value, and no-expression is the pattern to use otherwise.
# This expression also doesn't consume any characters, only detect if pattern matched.
address = re.compile(
    '''
    ^
    # 涉及到最后一个字符后面是否有空格或者特殊字符，可以参考 (?P<name>)，尽量给出verbose的pattern，把最后一个word之前的拆分出来，然后最后一个word，然后
    # 空格/特殊字符
    # 注意！：如果整个pattern有多个group/parts，re会尽可能让更多的group/parts都有match或者让整个pattern能够有match，参见最下面单独的的name email match。
    # 例如 no.brackets@example.com，如果只有name group，则会match: no.brackets(注意最后的s match了)，如果要同时search name和email group，则
    # name match: no.bracket, email match: s@example.com
    # 所以这里search no.brackets@example.com时，如果name match/consume了no.brackets, 则剩下的 @example.com不会match后续，整个pattern match失败，
    # 所以这里name group会选择no match，然后让后续都能match，从而整个pattern有match成功！
    # A name is made up of letters, and may include "."
    # for title abbreviations and middle initials.
    (?P<name>
       ([\w.]+\s+)*[\w.]+
     )?
    \s*

    # Email addresses are wrapped in angle brackets, but
    # only if a name is found.
    (?(name)
      # remainder wrapped in angle brackets because
      # there is a name, look ahead (?=) doesn't consume any characters
      (?P<brackets>(?=(<.*>$)))
      |
      # remainder does not include angle brackets without name
      (?=([^<].*[^>]$))
     )

    # Look for a bracket only if the look-ahead assertion
    # found both of them. here < OR \s* consumes characters
    (?(brackets)<|\s*)

    # The address itself: username@domain.tld
    (?P<email>
      [\w\d.+-]+       # username
      @
      ([\w\d.]+\.)+    # domain name prefix
      (com|org|edu)    # limit the allowed top-level domains
     )

    # Look for a bracket only if the look-ahead assertion
    # found both of them.
    (?(brackets)>|\s*)

    $
    ''',
    re.VERBOSE)

candidates = [
    u'First Last <first.last@example.com>',
    u'No Brackets first.last@example.com',
    u'Open Bracket <first.last@example.com',
    u'Close Bracket first.last@example.com>',
    u'no.brackets@example.com',
]

for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print('  Match name :', match.groupdict()['name'])
        print('  Match email:', match.groupdict()['email'])
    else:
        print('  No match')
    print()


print()
print('------------')
print()

test = re.compile(
    '''
    ^
    # 涉及到最后一个字符后面是否有空格或者特殊字符，可以参考 (?P<name>)，尽量给出verbose的pattern，把最后一个word之前的拆分出来，然后最后一个word，然后
    # 空格/特殊字符
    # A name is made up of letters, and may include "."
    # for title abbreviations and middle initials.
    (?P<name>
       ([\w.]+\s+)*[\w.]+
     )?
    \s*
    
    # The address itself: username@domain.tld
    (?P<email>
      [\w\d.+-]+       # username
      @
      ([\w\d.]+\.)+    # domain name prefix
      (com|org|edu)    # limit the allowed top-level domains
     )
    ''',
    re.VERBOSE)

for candidate in candidates:
    print('Candidate:', candidate)
    match = test.search(candidate)
    if match:
        print('  Match name :', match.groupdict()['name'])
        print('  Match email:', match.groupdict()['email'])
    else:
        print('  No match')
    print()

