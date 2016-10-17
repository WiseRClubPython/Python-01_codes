#!/usr/bin/env python
# -*- coding:utf-8 -*-

def get_pow(x, n):
    if n == 0:
        return 1
    else:
        return x * get_pow(x, n-1)


print get_pow(2,10)


def get_fact(n):
    if n == 1:
        return 1
    else:
        return n * get_fact(n-1)

print get_fact(10)


def get_fabs(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return get_fabs(n-1) + get_fabs(n-2)

print get_fabs(10)