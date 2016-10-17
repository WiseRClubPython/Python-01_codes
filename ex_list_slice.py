#!/usr/bin/env python
# -*- coding:utf-8 -*-

li = range(20)

print 'li = ', li

print li[0:10:2]
print li[-10:-1]
print li[-1::-1]
print li[:10]


li[10:10] = [100,200]
print li
del li[10:12]
print li