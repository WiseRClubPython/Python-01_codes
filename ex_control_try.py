#!/usr/bin/env python
# -*- coding:utf-8 -*-


while True:
    try:
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
    except:
        print 'Please type in a number.'
    finally:
        print 'Thanks!'