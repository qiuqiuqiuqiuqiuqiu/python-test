#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

s = socket.socket()
host = socket.gethostname()
print host
port = 12345
s.bind(('localhost', port))

s.listen(5)
while True:
    c, addr = s.accept()
    print "connection address: ", addr
    c.send("welcome to python!")
    c.close()
