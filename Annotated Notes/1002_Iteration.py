#!/usr/bin/env python

# ------------
# Iteration.py
# ------------

import itertools
import operator
import types

print "Iteration.py"

a = [2, 3, 4]
s = 0
for v in a :
    s += v
assert s == 9

a = [2, 3, 4]
for v in a :
    v += 1            # ?
assert a == [2, 3, 4]

a = ["abc", "def", "ghi"]
for v in a :
    v += "x"                      # ?
assert a == ["abc", "def", "ghi"]

a = [[2], [3], [4]]
for v in a :
    v += (5,)                        # ?
assert a == [[2, 5], [3, 5], [4, 5]]

a = [(2,), (3,), (4,)]
for v in a :
    v += (5,)                  # ?
assert a == [(2,), (3,), (4,)]

a = [(2, "abc"), (3, "def"), (4, "ghi")]
s = 0
for u, v in a :
    s += u
assert s == 9

d = {2 : "abc", 3 : "def", 4 : "ghi"}
s = 0
for k in d :
    s += k
assert s == 9

d = {2 : "abc", 3 : "def", 4 : "ghi"}
s = 0
for k, v in d.items() :
    s += k
assert s == 9

x = range(10)
assert type(x) is list
assert x       == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x = range(2, 10)
assert type(x) is list
assert x       == [2, 3, 4, 5, 6, 7, 8, 9]

x = range(2, 10, 2)
assert type(x) is list
assert x       == [2, 4, 6, 8]

x = range(10, 2, -2)
assert type(x) is list
assert x       == [10, 8, 6, 4]

x = xrange(10)
assert type(x) is xrange
assert x       != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert x[0]    == 0
assert x[9]    == 9
try :
    assert x[10] == 10                           # error: out of range
    assert False
except IndexError :
    pass
#x[0] = 2                                        # TypeError: 'xrange' object does not support item assignment
s = 0
for v in x :
    s += v
assert s == 45

x = xrange(15)
s = 0
for v in x :
    if v == 10 :
        break
    s += v
else :           # else clause in a for loop
    assert False # executes when the loop terminates normally
assert s == 45

x = itertools.count(0)            # 0, 1, 2, ...
assert type(x) is itertools.count
#assert x[0] == 0                 # TypeError: 'itertools.count' object is not indexable
s = 0
for v in x :
    if v == 10 :
        break
    s += v
assert s == 45

x = itertools.count(3, 2) # 3, 5, 7, 9, ...
s = 0
for v in x :
    if v > 10 :
        break
    s += v
assert s == 24

class My_XRange (object) :
    def __init__ (self, b, e) :
        self.b = b
        self.e = e

    def __iter__ (self) :
        return self

    def next (self) :
        if self.b == self.e :
            raise StopIteration()
        v       = self.b
        self.b += 1
        return v

x = My_XRange(0, 3)
assert type(x)  is My_XRange
assert iter(x)  is x
assert x.next() == 0
assert x.next() == 1
assert x.next() == 2
try :
    assert x.next() == 3
    assert False
except StopIteration, e :
    pass

s = 0
for v in My_XRange(0, 10) :
    s += v
assert s == 45

def my_xrange (b, e) :
    while b != e :
        yield b
        b += 1

x = my_xrange(0, 3)
assert type(x)  is types.GeneratorType
assert iter(x)  is x
assert x.next() == 0
assert x.next() == 1
assert x.next() == 2
try :
    assert x.next() == 3
    assert False
except StopIteration, e :
    pass

s = 0
for v in my_xrange(0, 10) :
    s += v
assert s == 45

x = (v for v in xrange(0, 3))
assert type(x)  is types.GeneratorType
assert iter(x)  is x
assert x.next() == 0
assert x.next() == 1
assert x.next() == 2
try :
    assert x.next() == 3
    assert False
except StopIteration, e :
    pass

s = 0
for v in (v for v in xrange(0, 10)) :
    s += v
assert s == 45

x = [2, 3, 4, 5, 6]
y = []
for v in x :
    y += [v * 5]
assert x == [ 2,  3,  4,  5,  6]
assert y == [10, 15, 20, 25, 30]

x = [2, 3, 4, 5, 6]
y = [v * 5 for v in x]                 # list comprehension
assert type(y) is list
assert x       == [2,   3,  4,  5,  6]
assert y       == [10, 15, 20, 25, 30]

x = [2, 3, 4, 5, 6]
y = map(lambda v : v * 5, x)
assert type(y) is list
assert x       == [2,   3,  4,  5,  6]
assert y       == [10, 15, 20, 25, 30]

x = [2, 3, 4, 5, 6]
y = []
for v in x :
    if v % 2 :
        y += [v * 5]
assert x == [2, 3, 4, 5, 6]
assert y == [15, 25]

x = [2, 3, 4, 5, 6]
y = [v * 5 for v in x if v % 2]
assert x == [2, 3, 4, 5, 6]
assert y == [15, 25]

x = [2, 3, 4, 5, 6]
y = map(lambda v : v * 5, filter(lambda u : u % 2, x))
assert x == [2, 3, 4, 5, 6]
assert y == [15, 25]

x = [2, 3, 4]
y = [4, 5]
z = []
for v in x :
    for w in y :
        z += [v + w]
assert x == [2, 3, 4]
assert y == [4, 5]
assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
assert z == [6, 7, 7, 8, 8, 9]

x = [2, 3, 4]
y = [4, 5]
z = [v + w for v in x for w in y]
assert x == [2, 3, 4]
assert y == [4, 5]
assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
assert z == [6, 7, 7, 8, 8, 9]

x = [2, 3, 4]
y = [4, 5]
t = map(lambda v : map(lambda w : v + w, y), x)
assert t == [[6, 7], [7, 8], [8, 9]]
z = sum(t, [])
assert x == [2, 3, 4]
assert y == [4, 5]
assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
assert z == [6, 7, 7, 8, 8, 9]

assert zip()                       == []
assert zip([])                     == []
assert zip((), ())                 == []
assert zip([2, 3])                 == [(2,), (3,)]
assert zip((2, 3), (4, 5), (6, 7)) == [(2, 4, 6), (3, 5, 7)]
assert zip([2, 3, 4], [5, 6, 7])   == [(2, 5), (3, 6), (4, 7)]

print "Done."
