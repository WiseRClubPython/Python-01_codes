#!/usr/bin/env python
# -*- coding:utf-8 -*-
from copy import deepcopy


d1 = {'Mike':100, 'Jim':99, 'Brad':98}
print 'd1 = ', d1
print 'd1["Mike"] = ', d1['Mike']
d1['Mike'] = 0
print 'd1["Mike"] = 0 then d1["Mike"] = ', d1['Mike']
print 'd1.get("Hellen") = ', d1.get('Hellen')

print 'd1.items() = ', d1.items()
print 'd1.keys() = ', d1.keys()
print 'd1.has_key("Hellen") = ',d1.has_key("Hellen")
print d1.pop("Mike")  # try d1.popitem()
print 'd1.pop("Mike") then d1 = ', d1


d1['Hellen'] = [99, 100]

print 'd1["Hellen"] = [99, 100] then d1 = ', d1
d2 = d1.copy()
print 'd2 = d1.coy() then d2 = ',d2
d2['Hellen'].append(101)

print 'd2["Hellen"].append(101) then d1 = ' , d1

d3 = deepcopy(d1)
print 'd3 = deepcopy(d1) then d3 = ', d3
d3['Hellen'].append(102)
print 'd3["Hellen"].append(102) then d1 = ', d1
print 'd3 = ', d3

for i in d1:
    print d1[i]

del d1["Jim"]
print 'del d1["Jim"] then d1 = ', d1
d1.clear()

print 'dl.clear() then d1 = ', d1