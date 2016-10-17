#!/usr/bin/env python
# -*- coding:utf-8 -*-

list_of_tuples = [('Mike','Python'),('Jim','Ruby'),('Brad','PHP')]

d = {key: value for key, value in list_of_tuples}
print d
print {val: key for key, val in d.items()}
