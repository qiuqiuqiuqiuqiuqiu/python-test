#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
print re.match('www', 'www.runoob.com').span()
print re.match('com', 'www.runoob.com')

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print "matchObj.group(): ", matchObj.group()
    print "matchObj.group(1): ", matchObj.group(1)
    print "matchObj.group(2): ", matchObj.group(2)
else:
    print "no match"

print re.search('www', 'www.runoob.com').span()
print re.search('com', 'www.runoob.com').span()


phone = "2004-959-559 # this is international phone number"
num = re.sub(r'#.*$', "", phone)
print "phone number is", num
num = re.sub(r'\D', "", phone)
print "phone number is", num


def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print re.sub('(?P<value>\d+)', double, s)
print re.sub('(?P<value>\d+)', "", s)

pattern = re.compile(r'\d+')
print pattern.match('one12twothree34four', 3, 10).group()
print pattern.findall('runoob 123 google 456')
print pattern.findall('run88oob123google456', 0, 10)

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print match.group()

print re.split('\W+', 'runoob, runoob, runoob.')