#! /usr/bin/env python
# -*- coding:utf-8 -*-

import re

m1 = re.search('\d+', 'abc123')
if m1 is not None:
    print m1.group()


m2 = re.match('.*', 'abc123')
if m2 is not None:
	print m2.group()



