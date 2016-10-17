#!/usr/bin/env python
# -*- coding:utf-8 -*-

#import ex_module

from . import ex_module

from packages import ex_module_sub
#import ex_module
from ex_module import get_fabs
#from ex_module import *

#ex_module.say_hello("Julia")
ex_module_sub.say_hi('Julia')
ex_module.say_hello('Julia')
print get_fabs(10)
