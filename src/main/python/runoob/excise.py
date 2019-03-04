#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import calendar
from src.runoob import support
import math

print "Hello World!"

print "你好"

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print days

item1 = 2
item2 = 5
item3 = 10
total = item1 + \
        item2 + \
        item3
print total

word = 'word'
sentence = "this is sentence"
paragraph = """"this is paragraph
include multi line"""

print total,days

a = b = c = 1
print a, b, c


s = 'abcdef'
print s[1:5]

print s[-5:-1]

print s*2
print s[2:]
print s + 'TEST'
print s[1:4:2]

t = ['a', 'b', 'c', 'd', 'e']
print t
print t[0]
print t[1:3]
print t[2:]
print t * 2

tuple = ('runoob', 786, 2.23, 'John', 70.2)
tinytuple = (123, 'john')
print tuple
print tuple[0]

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

print dict
print dict.keys()
print dict.values()


a=21;b=10;c=0;
print a+b
print a-b
print a*b
print a/b
print a%b
print a**b
print a//b

print a==b
print a!=b
print a<>b
print a<b
print a>b
print a<=b
print a>=b

num = 5
if num == 3:
    print 'boss'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
else:
    print 'roadman'

if num >= 0 and num <= 10:
    print 'hello'
else:
    print 'undefine'


numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print even
print odd


i = 2
while(i < 10):
    j = 2
    while(j <= (i/j)):
        if i%j == 0: break
        j += 1
    if(j > i/j): print i, " 是素数"
    i = i + 1

for letter in 'Python':
    pass

print "My name is %s and weight is %d kg!" % ('Zara', 70)


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = ['a','b']
dict['School'] = 'RUNOOB'
print dict
print type(dict)

print dict.popitem()

dict2 = dict.copy()
dict3 = dict.copy()
dict2['Age'].append('c')
dict3['Age'] = ['a','b','d']
print dict
print dict2
print dict3

ticks = time.time()
print ticks
localtime = time.localtime(time.time())
print localtime
localtime = time.asctime(localtime)
print localtime

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

print calendar.month(2016, 1)

print time.timezone
print time.tzname

def ChangeInt(a):
    a=10
b=2
ChangeInt(b)
print b

def ChangeMe(mylist):
    mylist.append([1,2,3,4])
    print mylist
    return
lista = [10,20,30]
ChangeMe(lista)
print lista


def printinfo(name, age):
    print "Name: ", name
    print "Age: ", age
    return
printinfo(age=50, name="Miki")

def printinfo1(arg1, *vartuple):
    print arg1
    for var in vartuple:
        print var
    return
printinfo1(10)
printinfo1(70,60,50)

sum = lambda arg1, arg2: arg1 + arg2
print sum(10, 20)

support.print_func("Runoob")
print dir(math)