#!/usr/bin/env python
# -*- coding:utf-8 -*-


n = raw_input('Type in a number:')
n = int(n)
x = 99

if n < x:
    print('It is too small.')
elif n > x:
    print('It is too big.')
else:
    print('You are right.')


n = raw_input('Type in a number again:')
n = int(n)
if n < x or n > x:
    print('You are wrong.')
else:
    print('You are right.')