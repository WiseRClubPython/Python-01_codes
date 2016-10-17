#!/usr/bin/env python
# -*- coding:utf-8 -*-


while True:
    n = raw_input('Type in a number:')
    n = int(n)
    x = 99
    
    if n < x:
        print('It is too small.')
    elif n > x:
        print('It is too big.')
    else:
        print('You are right.')
        break