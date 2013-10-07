#!/usr/bin/env python

"""
CS373: Quiz #10 (5 pts)
"""

""" ----------------------------------------------------------------------
 1. In the paper, "A Bug and a Crash" about the Ariane 5, what was the
    software bug?
    (1 pt)

the conversion of a 64-bit number to a 16-bit number
"""

""" ----------------------------------------------------------------------
 2. In the paper, "Mariner 1", what was the software bug?
    (1 pt)

the ommission of a hyphen
"""

""" ----------------------------------------------------------------------
 3. Define the function map().
    (2 pts)
"""

def map (f, a) :
    return [f(v) for v in a]

assert map(lambda x : x * x, [])     == []
assert map(lambda x : x * x, [2])    == [4]
assert map(lambda x : x * x, [2, 3]) == [4, 9]

assert map(lambda x : x * x * x, [])     == []
assert map(lambda x : x * x * x, [2])    == [8]
assert map(lambda x : x * x * x, [2, 3]) == [8, 27]
