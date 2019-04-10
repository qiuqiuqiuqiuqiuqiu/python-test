#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# 改变当前目录
os.chdir("../../resources/")

# 打开一个文件
fo = open("foo.txt", "w+")
print "file name: ", fo.name
print "is closed: ", fo.closed
print "access mode: ", fo.mode
print "is add space at the end: ", fo.softspace
# write可以将字符串写入文件，r/r+/w/w+方式打开时，指针在开头
# a/a+方式打开时，指针在结尾
fo.write("www.runoob.com!\nVery good site!\n")
# 关闭打开的文件
fo.close()


fo = open("foo.txt", "r+")
str = fo.read(15)
print "读取的字符串是：", str
# 查找当前位置
position = fo.tell()
print "当前位置：", position

# 把指针重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(15)
print "重新读取的字符串：", str
fo.close()

os.rename("foo.txt", "foo2.txt")
# os.remove("foo2.txt")

os.mkdir("test")
os.rmdir("test")
