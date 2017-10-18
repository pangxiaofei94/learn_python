# -*- coding: utf-8 -*-

import functools

def log(text=''):
	def decor(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('begin call:')
			abc = func(*args, **kw)
			print('end call:')
			return abc
		return wrapper
	return decor

@log()
def f():
	print('zhixing')

f()
'''
def count():
	def f(j):
		return lambda  :j * j
	fs = []
	return [f(i) for i in range(1,4)]
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
'''

'''
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
		print(fs)
	return fs

f1, f2, f3 = count()
'''