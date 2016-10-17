#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

if len(sys.argv) > 1:   
    filename = sys.argv[1]
    print('The file name is ', filename)
    print('Open file now')
    f = open(filename)
    for i in f:
        print(i)
    f.close

with open(raw_input('Type in another file name:')) as f2:
    for i in f2:
        print(i)


f3 = open(raw_input('Type in a file name:'),'w')
l1 = raw_input('Line1:')
l2 = raw_input('Line2:')

f3.write(l1+'\n')
f3.write(l2+'\n')
f3.close
