#!/usr/bin/env python
# -*- coding:utf-8 -*-


l1 = ['Mike', 'Jim', 'Brad']
print 'l1 = ', l1
l2 = ['Julia',]
print 'l2 = ', l2
l3 = []
print 'l3 = ', l3 

l4 = l1 + l2 + l3
print 'l4 = ', l4

l5 = l1 * 2
print 'l5 = ', l5

l4.append('Hellen')
print "l4.append('Hellen') then l4 = ", l4
l4.insert(0, 'Bob')
print "l4.insert(0, 'Bob') then l4 = ", l4
print l4.pop()
print "l4.pop() then l4 = ",l4
l4.sort()
print "l4.sort() then l4 = ",l4
l4.reverse()
print "l4.reverse() then l4 = ",l4
l4.extend(l2)
print "l4.extend(l2) then l4 = ",l4
l4.remove('Julia')
print "l4.remove('Julia') then l4 = ",l4
del l4[0]
print "del l4[0] then l4 = ",l4


l6 = ['Mike', 'Jim', 'Brad', ['Java', 'Python'], 100, 200]
print l6
print l6[-3][1]


for i in l6:
    print i
