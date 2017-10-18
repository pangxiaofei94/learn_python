# -*- coding: utf-8 -*-
# 

class MyshinyClass(object):
	"""docstring for MyshinyClass"""
	pass

MyshinyClass = type('MyshinyClass', (), {})

print(MyshinyClass)
print(MyshinyClass())
		