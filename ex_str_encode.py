#!/usr/bin/env python
# -*- coding:utf-8 -*-


e = 'a'
c = '中'

print 'e = ', e
print 'c = ', c
print 'repr(e) = ', repr(e)
print 'repr(c) = ', repr(c)

e = u'a'
c = u'中'
print 'e = ', e
print 'c = ', c
print 'repr(e) = ', repr(e)
print 'repr(c) = ', repr(c)


e = 'a'
c = '中'
print 'e = ', e
print 'c = ', c.decode('utf-8')
print 'repr(e) = ', repr(e)
print 'repr(c) = ', repr(c.decode('utf-8'))


d = raw_input('输入：'.decode('utf-8').encode('GB2312'))
print d