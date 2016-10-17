#!/usr/bin/env python
# -*- coding:utf-8 -*-
def foo():
    yield 1
    yield 2
    yield 3

for i in foo():
    print i

print '-' * 20

def foo2(how_many):
    for number in range(how_many):
        if number**2 > 3:
            yield number * 2

for number in foo2(5):
    print number

print '-' * 20

gen = (2*x for x in range(5) if x**2 > 3)
for number in gen:
    print number



