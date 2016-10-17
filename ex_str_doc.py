#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo(object):
    """It does things."""
    def __init__(self, thing):
        """A Foo needs a thing to do."""
        self.thing = thing
    def do(self):
        """Do the thing!"""
        print "Doing..."
        return Bar(thing)

class Bar(object):
    """A thing which has been done."""
    def __init__(self, thing):
        """Make a thing into a done thing."""
        self.thing = thing