#!/usr/bin/env python
# -*- coding:utf-8 -*-

def foo(*params):
    for i in params:
        print i


def bar(**kwparams):
    for i in kwparams:
        print kwparams[i]

foo(1,2,3,4,5)
bar(a=1,b=2,c=3,d=4,e=5)

print '-' * 20

def foo2(a,b,c):
    print a,b,c

def bar2(a=1,b=2,c=3):
    print a,b,c

p1 = (1,2,3)
p2 = {'a':1,'b':2,'c':3}

foo2(*p1)
bar2(**p2)

print '-' * 20

def foo3(a,b,*params):
    print a,b
    print params

def bar3(a,b,**kwparams):
    print a,b
    print kwparams

foo3(1,2,3,4,5)
bar3(1,2,c=3,d=4,e=5)

print '-' * 20

def foo4(*params,**kwparams):
    print params
    print kwparams

foo4(1,2,c=3,d=4,e=5)



