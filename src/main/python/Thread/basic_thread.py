#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time


# 为线程定义一个函数
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (thread_name, time.ctime(time.time()))


# 创建两个线程
try:
    # 线程函数的参数，必须为tuple元组类型
    # 元组类型与列表类似，不同之处在于元组不能修改，元组使用小括号，列表使用中括号
    # 元组使用逗号分割，只有一个元素时，要在元素后面添加逗号
    thread.start_new_thread(print_time, ("Thread-1", 2, ))
    thread.start_new_thread(print_time, ("Thread-2", 4, ))
except:
    print "Error: unable to start thread"

while 1:
    pass
