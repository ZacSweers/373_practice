#!/usr/bin/env python

"""
CS373: Quiz #13 (5 pts)
"""

""" ----------------------------------------------------------------------
 1. Fill in the TWO blanks below:
    [The Open-Closed Principle]
    (2 pts)

    Software entities (classes, modules, functions, etc.) should be open
    for <BLANK>, but closed for <BLANK>.

extension
modification
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following program?
    (2 pts)

[[2, 5], [3, 5], [4, 5]]
[(2,), (3,), (4,)]
"""

a = [[2], [3], [4]]
for v in a :
    v += (5,)
print a

a = [(2,), (3,), (4,)]
for v in a :
    v += (5,)
print a
