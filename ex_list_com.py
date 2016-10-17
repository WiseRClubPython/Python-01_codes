#!/usr/bin/env python
# -*- coding:utf-8 -*-

series = range(10)

def do_pow(item):
	return item ** 2

print [item for item in series]
print [do_pow(item) for item in series]
print [do_pow(item) for item in series if item > 4]

print '-' * 20

booze = ['beer', 'wine', 'scotch', 'gin']
soft_drinks = ['water', 'soda', 'juice']
print [(x, y) for x in booze for y in soft_drinks]

print [x for x in zip(booze, soft_drinks)]


print {v for v in 'My Python' if v not in 'thon'}
