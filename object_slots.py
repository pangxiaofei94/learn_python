# -*- coding: utf-8 -*-

from types import MethodType
class Student(object):
	
	pass


def set_age(self, age):
		self.age = age

s = Student()
# s.name = 'pangxiaofei'
# print(s.name)
s.set_age = MethodType(set_age, s)
s.set_age(26)
print(s.age)

Student.set_age = set_age
s2 = Student()

s2.set_age(27)
print(s2.age)