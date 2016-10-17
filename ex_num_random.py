#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

print 'choice(range(10)) = ', random.choice(range(10))
print 'randrange(0,10,2) = ', random.randrange(0,10,2)
print 'random() = ', random.random()
print 'uniform(10,20) = ', random.uniform(10,20)

a = [1,2,3,4]
random.shuffle(a)
print 'shuffle([1,2,3,4]) then ', a