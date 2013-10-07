#!/usr/bin/env python

# --------
# Types.py
# --------

import sys
import types

print "Types.py"

b = True
b = False
assert type(b)    is bool
assert type(bool) is type

i = 2
assert type(i)   is int
assert type(int) is type

j = 2L
assert type(j)    is long
assert type(long) is type

f = 2.3
assert type(f)     is float
assert type(float) is type

c = 2 + 3j
assert type(c)       is complex
assert type(complex) is type

s = 'abc'
s = "abc"
assert type(s)   is str
assert type(str) is type

l = [2, "abc", 3.45]
assert type(l)    is list
assert type(list) is type

t = (2, "abc", 3.45)
assert type(t)     is tuple
assert type(tuple) is type

s = set([2, "abc", 3.45])
assert type(s)   is set
assert type(set) is type

d = {2 : "def", 3.45 : 3, "abc" : 6.78}
assert type(d)    is dict
assert type(dict) is type

class A (object) :
    def __init__ (self, i, d, x) :
        self.i = i
        self.d = d
        self.x = x

class B (A) :
    pass

x = A(2, 3.45, "abc")
assert type(x) is A
assert type(A) is type

y = B(2, 3.45, 6)
assert type(y) is B
assert type(B) is type

assert     issubclass(bool, int)
assert not issubclass(int,  long)

assert issubclass(A, object)
assert issubclass(A, A)

assert issubclass(B, object)
assert issubclass(B, A)
assert issubclass(B, B)

def inc (v) :
    return v + 1

assert type(inc)                is types.FunctionType
assert type(types.FunctionType) is type

print "Done."
