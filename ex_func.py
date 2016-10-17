#!/usr/bin/env python
# -*- coding:utf-8 -*-

def say_hello(x):
	print('Hello, ' + x)



def get_fabs(num):
    f = [0,1]
    while num > 0:
        f.append(f[-1] + f[-2])
        num -= 1
    return f


say_hello('Mike')
f = get_fabs(10)
for i in f:
    print i