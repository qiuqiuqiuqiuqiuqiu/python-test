#!/usr/bin/python
# -*- coding: UTF-8 -*-

def runoob2():
    print "I'm in runoob2"

try:
    fh = open("../../resources/testfile", "w")
    fh.write("this is a test")
except IOError, err:
    print "IOError",err
else:
    print "write scucess"


try:
    fh = open("../../resources/testfile", "w")
    fh.write("this is a test")
except IOError, err:
    print "IOError", err
finally:
    print "this is finally"