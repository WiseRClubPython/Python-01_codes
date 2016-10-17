#!/usr/bin/env python
# -*- coding: UTF-8 -*-


count = 5

for i in range(count):
    if i == 0:
        continue
    print i


for i in range(count):
    if i == 0:
        continue
    
    n = raw_input('Type in a number:')
    n = int(n)
    x = 99
    
    if n < x:
        print('It is too small. %d chances left.' % (count - i - 1))
    elif n > x:
        print('It is too big. %d chances left.' % (count - i - 1))
    else:
        print('You are right.')
        break