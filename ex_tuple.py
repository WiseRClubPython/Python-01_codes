#!/usr/bin/env python
# -*- coding:utf-8 -*-


t1 = (1,2)
print 't1 = ',  t1
t2 = (3,)
print 't2 = ',  t2
t3 = ()
print 't3 = ',  t3


t4 = t1 + t2 + t3
print 't4 = ', t4
t5 = t1 * 2
print 't5 = ',  t5


print 't4[2] = ', t4[2]

print '3 in t4 =' ,3 in t4

for i in t4:
    print i