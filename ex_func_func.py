#!/usr/bin/env python
# -*- coding:utf-8 -*-

def square(x):
    return x * x

a = range(10)
print map(square, a)
print map(lambda x : x * x, a)

def add(x,y):
    return x + y

print reduce(add, a)
print reduce(lambda x, y : x + y, a)

def morethan(x):
    return x > 5

print filter(morethan, a)
print filter(lambda x : x > 5, a)

def order(x):
    return -x

print sorted(a, key = order)
print sorted(a, key = lambda x : -x)


def func_gen(*params):
    def func():
        return sum(params)
    return func

f = func_gen(1,2,3,4)
print f()
