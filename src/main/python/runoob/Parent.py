#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:
    parentAttr = 100
    def __init__(self):
        print "construct parent"

    def parentMethod(self):
        print "parent method"

    def setAttr(self,attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "parent attr:", Parent.parentAttr

    def myMthod(self):
        print "parent my method"

class Child(Parent):
    def __init__(self):
        print "construct child"

    def childMethod(self):
        print "child method"

    def myMthod(self):
        print "child my method"

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.myMthod()