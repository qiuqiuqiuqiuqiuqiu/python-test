#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "total employee %d" % Employee.empCount

    def displayEmployee(self):
        print "name: ", self.name, "salary: ", self.salary


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "total employee %d" % Employee.empCount

print hasattr(emp1, 'age')
# print getattr(emp1, 'age')
print setattr(emp1, 'age', 8)
print emp1
print delattr(emp1, 'age')
print emp1
print Employee.__doc__
print Employee.__name__
print Employee.__module__
print Employee.__bases__
print Employee.__dict__