#!/usr/bin/env python
# -*- coding:utf-8 -*-

counter = {}
s = "It is a beautifull day. A good day."
for char in s:
    if char not in counter:
        counter[char] = 1
    else:
        counter[char] += 1

print counter



from collections import Counter
counter = Counter(s)
print counter
for i in counter.items():
    print i