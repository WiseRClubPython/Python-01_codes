#!/usr/bin/env python
# -*- coding:utf-8 


def deco(func):
    def wrapper(*params, **kwParams):
        print "Before calling"
        func(*params, **kwParams)
        print "After calling"
    return wrapper


@deco
def say_hi(a):
    print "Hi,", a



say_hi("Julia")
