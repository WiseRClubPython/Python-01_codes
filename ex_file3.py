#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

print os.environ
path = os.path.abspath('.')
print path
path2 = os.path.join(path, 'files')
print path2

os.mkdir(path2)

os.rmdir(path2)

path3 = os.path.join(path, 'ex_file.txt')
print os.path.split(path3)
print os.path.splitext(path3)

print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']