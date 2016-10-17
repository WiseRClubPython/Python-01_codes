#!/usr/bin/env python
# -*- coding: UTF-8 -*-

a = 5
b = 2

print "a = ",a
print "a = ",b
print "a + b = ", a + b
print "a - b = ", a - b 
print "a * b = ", a * b 
print "a / b = ", a / b 
print "a % b = ", a % b
print "a ** b = ", a ** b 
print "a // b = ", a // b 

print "-" * 20
print "a > b = ", a > b 
print "a < b = ", a < b 
print "a <> b = ", a <> b 
print "a != b = ", a != b 
print "a >= b = ", a >= b 
print "a <= b = ", a <= b 

print "-" * 20
a += b
print "a += b then a = ", a
a -= b
print "a -= b then a = ", a
a *= b
print "a *= b then a = ", a
a /= b
print "a /= b then a = ", a
a %= b
print "a %= b then a = ", a
a **= b
print "a **= b then a = ", a
a //= b
print "a //= b then a = ", a

print "-" * 20
a = 5  # 00000101
b = 2  # 00000010
print "a & b = ", a & b 
print "a | b = ", a | b 
print "a ^ b = ", a ^ b 
c = ~a
print "~a = ", c
c = a << 2
print "a << 2 = ", c # 00010100
c = a >> 2
print "a >> 2 = ", c # 00000001
