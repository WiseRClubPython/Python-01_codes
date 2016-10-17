#!/usr/bin/env python
# -*- coding:utf-8 -*-

str1 = 'it is a beautifull day'

print 'str1 = ', repr(str1)
print 'str1.split() then ', str1.split()
print 'str1.capitalize() = ', str1.capitalize()
print 'str1.find("a") = ', str1.find("a")
print 'str1.index("a") = ', str1.index("a")
print 'str1.endswith("ay") = ', str1.endswith("ay")
print 'str1.startswith("it") = ', str1.startswith("it")
print 'str1.title() = ', str1.title()
print 'str1.upper() = ', str1.upper()
print 'str1.lower() = ', str1.lower()
print 'str1.replace("beautifull","bad") = ', str1.replace("beautifull", "bad")
print '",".join(str1.split()) = ', ",".join(str1.split())
print 'len(str1) = ' ,len(str1)

print '''Hello,
It's a beautifull day.
Let's go.'''