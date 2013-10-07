#!/usr/bin/env python

# ------------
# Arguments.py
# ------------

print "Arguments.py"

def f1 (j) :
    j += 1

i = 2
f1(i)
assert i is 2

def f2 (t) :
    t += "def"

s = "abc"
f2(s)
assert s is "abc"

def f3 (b) :
    b[1] += 1

a = [2, 3, 4]
f3(a)
assert a is not [2, 4, 4]
assert a ==     [2, 4, 4]

a = [2, 3, 4]
f3(a[:])
assert a is not [2, 3, 4]
assert a ==     [2, 3, 4]

def f4 (b) :
    b += (5,)

a = [2, 3, 4]
f4(a)
assert a is not [2, 3, 4, 5]
assert a ==     [2, 3, 4, 5]

a = [2, 3, 4]
f4(a[:])
assert a is not [2, 3, 4]
assert a ==     [2, 3, 4]

a = (2, 3, 4)
f4(a)
assert a is not (2, 3, 4)
assert a ==     (2, 3, 4)

print "Done."
