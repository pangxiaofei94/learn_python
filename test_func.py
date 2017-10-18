# -*- coding: utf-8 -*-
# 

def is_palindrome(n):
	if str(n) == str(n)[::-1]:
		return n

output = filter (is_palindrome, range(1, 1000))
print(list(output))
'''
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n >0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

for n in primes():
	if n < 50:
		print(n)
	else:
		break
'''
'''
from functools import reduce

def prod(L):
    def mult(x, y):
    	print('x:',x,'y:',y)
        # return x * y
    return reduce(mult,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
'''
# def normalize(name):
# 	return name[0].upper() + name[1::].lower()

# L1 = ['adam', 'LIST', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
# def triangles():
# 	L = [1]
# 	while True:
# 		yield L
# 		L = [L[i] + L[i+1] for i in range(len(L)-1)]
# 		L.insert(0,1)
# 		L.append(1)

# num = 0
# for n in triangles():
# 	print(n)
# 	num = num + 1
# 	if num == 5:
# 		break

'''
#关键字参数
def person(name, age, **kw):
	print('name:', name, ' age:', age, ' other:', kw)

# person('pangxiaofei', 27, city='Beijing')
# person('pangxiaofei', 27, gender='M', job='PHP')

extra = {'city':'Beijing', 'job':'PHP'}
person('pangxiaofei', 27, **extra)
'''