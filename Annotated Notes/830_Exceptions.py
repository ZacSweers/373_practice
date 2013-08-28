#!/usr/bin/env python

# -------------
# Exceptions.py
# -------------

print "Exceptions.py"

def f (b) :
    if b :
        raise NameError("abc")
    return 0

try :
    assert f(False) == 0
except NameError :
    assert False

try :
    assert f(True) == 1
    assert False
except NameError, e :
    assert type(e)      is     NameError
    assert type(e.args) is     tuple
    assert len(e.args)  ==     1
    assert e.args       is not ("abc",)
    assert e.args       ==     ("abc",)
else :
    assert False

assert issubclass(NameError,     Exception)
assert issubclass(Exception,     BaseException)
assert issubclass(NameError,     BaseException)
assert issubclass(BaseException, object)

print "Done."
