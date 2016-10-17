#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo(object):
    def __init__(self, thing):
        self.thing = thing
    def __enter__(self):
        print "Preparing to do..."
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        print "Done!"
    def do(self):
        print "Doing " + self.thing

with Foo('something') as f:
    f.do()

    