#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from os.path import exists

s, from_filename, to_filename = sys.argv

print('Copy from %s to %s' % (from_filename, to_filename))
from_file = open(from_filename)
data = from_file.read()
print('The file size is %d', len(data))
from_file.close

if exists(to_filename):
    print('The file exists. hit ENTER to continue, CTRL+C to abort')
    raw_input()

to_file = open(to_filename,'w')
to_file.write(data)
to_file.close
