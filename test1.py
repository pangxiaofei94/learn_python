# -*- coding: utf-8 -*-

import test_sys
# for i in range(4):
# 	for row in matrix:
# 		row[i]
# a = ['adam', 'LISA', 'barT']
# def firstToUpper(a):
# 	return a.capitalize()
# b = list(map(firstToUpper, a))

# print(b);


# def triangles(max):
# 	n = 1
# 	while n <= max:
# 		if n == 1:
# 			a = [1]
# 			n = n+1
# 			yield a
# 		elif n == 2:
# 			a = [1,1]
# 			n = n+1
# 			yield a
# 		else:
# 			# print('a:', a)
# 			a = [1] + [a[x-1] + a[x] for x in range(1,n-1)] + [1]
# 			n = n+1
# 			yield a

# maxnum = int(input('请输入数字：'))

# for k in triangles(maxnum):
# 	print(k)


# import os
# listdir = [d for d in os.listdir('.')]
# print(listdir)


# import urllib.request

# params = {"username":"827464561@qq.com", "password":"pxf15313111209"}
# data = urllib.parse.urlencode(params)
# print(data)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib.request.Request(url, data)
# response = urllib.request.urlopen(request)
# # response = urllib.request.urlopen("http://www.baidu.com")

# print(response.read())